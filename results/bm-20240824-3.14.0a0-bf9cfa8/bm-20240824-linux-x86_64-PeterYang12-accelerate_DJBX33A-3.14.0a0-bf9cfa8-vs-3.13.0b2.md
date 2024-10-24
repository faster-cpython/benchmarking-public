# Results vs. 3.13.0b2

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                     |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                   |
| html5lib       | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                      | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 388 ms: 1.19x faster                                                     |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                             |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                    |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                     |
| float          | 78.9 ms                                                    | 76.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 126 ms: 1.08x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.48 ms: 1.05x faster                                                    |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                      | 1.04x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                     |
| xml_etree_generate   | 87.4 ms                                                    | 84.6 ms: 1.03x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                     |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                     |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 21.5 ms: 1.10x faster                                                    |
| genshi_xml      | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                    |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                    |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                     |
| deepcopy_memo              | 39.7 us                                                    | 29.0 us: 1.37x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.72 us: 1.23x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 388 ms: 1.19x faster                                                     |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.55 ms: 1.16x faster                                                    |
| richards                   | 50.9 ms                                                    | 45.8 ms: 1.11x faster                                                    |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                     |
| logging_silent             | 105 ns                                                     | 94.5 ns: 1.11x faster                                                    |
| genshi_text                | 23.7 ms                                                    | 21.5 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                    |
| scimark_fft                | 392 ms                                                     | 359 ms: 1.09x faster                                                     |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                     |
| regex_compile              | 137 ms                                                     | 126 ms: 1.08x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                     |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                     |
| thrift                     | 823 us                                                     | 768 us: 1.07x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 72.4 ms: 1.07x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                                    |
| bench_thread_pool          | 834 us                                                     | 780 us: 1.07x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                   |
| pyflate                    | 484 ms                                                     | 454 ms: 1.07x faster                                                     |
| genshi_xml                 | 51.6 ms                                                    | 48.6 ms: 1.06x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 714 ms: 1.06x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 479 ms: 1.06x faster                                                     |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                    |
| sympy_sum                  | 156 ms                                                     | 147 ms: 1.06x faster                                                     |
| sympy_str                  | 282 ms                                                     | 267 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                    |
| spectral_norm              | 116 ms                                                     | 110 ms: 1.06x faster                                                     |
| sympy_integrate            | 20.5 ms                                                    | 19.4 ms: 1.05x faster                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.48 ms: 1.05x faster                                                    |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.65 sec: 1.05x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                    |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.56 ms: 1.05x faster                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 53.1 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 896 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.82 sec: 1.04x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                    |
| sympy_expand               | 473 ms                                                     | 455 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                    |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                     |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.03x faster                                                     |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.03x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 84.6 ms: 1.03x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                   |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                    |
| raytrace                   | 267 ms                                                     | 259 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                     |
| hexiom                     | 6.30 ms                                                    | 6.12 ms: 1.03x faster                                                    |
| nbody                      | 88.3 ms                                                    | 86.0 ms: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.03x faster                                                     |
| async_generators           | 442 ms                                                     | 431 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                     |
| float                      | 78.9 ms                                                    | 76.9 ms: 1.03x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                   |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                    |
| nqueens                    | 81.4 ms                                                    | 79.7 ms: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                     |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                   |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                    |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.34 ms: 1.01x faster                                                    |
| fannkuch                   | 402 ms                                                     | 399 ms: 1.01x faster                                                     |
| json                       | 5.31 ms                                                    | 5.26 ms: 1.01x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                    |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                                    |
| go                         | 145 ms                                                     | 159 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                             |

Benchmark hidden because not significant (5): async_tree_io, scimark_monte_carlo, regex_v8, coroutines, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.01x