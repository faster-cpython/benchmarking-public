# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 261 ms: 1.05x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                 |
| html5lib       | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                      | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 370 ms: 1.20x faster                                                   |
| async_tree_none            | 378 ms                                                     | 318 ms: 1.19x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 287 ms: 1.17x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                   |
| async_tree_io              | 939 ms                                                     | 820 ms: 1.15x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.15x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| nbody          | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.8 ms: 1.05x faster                                                  |
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                   |
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                  |
| json_loads           | 28.9 us                                                    | 27.8 us: 1.04x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                   |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 49.7 ms: 1.04x faster                                                  |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                  |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 370 ms: 1.20x faster                                                   |
| async_tree_none            | 378 ms                                                     | 318 ms: 1.19x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 287 ms: 1.17x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 400 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.59 ms: 1.15x faster                                                  |
| async_tree_io              | 939 ms                                                     | 820 ms: 1.15x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.53 ms: 1.13x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.51 sec: 1.11x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                   |
| richards                   | 50.9 ms                                                    | 46.6 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                   |
| richards_super             | 57.4 ms                                                    | 53.1 ms: 1.08x faster                                                  |
| scimark_fft                | 392 ms                                                     | 363 ms: 1.08x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 72.1 ms: 1.07x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 786 us: 1.06x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 23.8 ms: 1.05x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 90.0 ms: 1.05x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.16 us: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.69 sec: 1.05x faster                                                 |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                   |
| 2to3                       | 274 ms                                                     | 261 ms: 1.05x faster                                                   |
| telco                      | 8.41 ms                                                    | 8.03 ms: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.05x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                   |
| sympy_sum                  | 156 ms                                                     | 149 ms: 1.04x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.4 ms: 1.04x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                                  |
| dulwich_log                | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                                  |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.8 us: 1.04x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 49.7 ms: 1.04x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                                  |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                  |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 734 ms: 1.03x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                  |
| pyflate                    | 484 ms                                                     | 469 ms: 1.03x faster                                                   |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                   |
| raytrace                   | 267 ms                                                     | 258 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                   |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 79.1 ms: 1.03x faster                                                  |
| float                      | 78.9 ms                                                    | 76.7 ms: 1.03x faster                                                  |
| spectral_norm              | 116 ms                                                     | 113 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                  |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                                   |
| go                         | 145 ms                                                     | 141 ms: 1.02x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 85.6 ms: 1.02x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.16 ms: 1.02x faster                                                  |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.02x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                   |
| nbody                      | 88.3 ms                                                    | 86.9 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                   |
| coverage                   | 93.1 ms                                                    | 91.7 ms: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                   |
| async_generators           | 442 ms                                                     | 438 ms: 1.01x faster                                                   |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| generators                 | 29.6 ms                                                    | 29.9 ms: 1.01x slower                                                  |
| fannkuch                   | 402 ms                                                     | 408 ms: 1.01x slower                                                   |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.02x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                           |

Benchmark hidden because not significant (5): pylint, deltablue, comprehensions, coroutines, tomli_loads
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x