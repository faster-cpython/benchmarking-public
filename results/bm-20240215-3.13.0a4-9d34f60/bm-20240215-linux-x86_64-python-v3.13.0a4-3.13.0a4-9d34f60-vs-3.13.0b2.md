# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.00x slower
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 269 ms: 1.02x faster                                       |
| chameleon      | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                      |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                     |
| tornado_http   | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 444 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 718 ms: 1.18x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 571 ms: 1.23x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 733 ms: 1.25x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.22 sec: 1.31x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 585 ms: 1.32x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 455 ms: 1.35x slower                                       |
| Geometric mean             | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| nbody          | 88.3 ms                                                    | 92.1 ms: 1.04x slower                                      |
| float          | 78.9 ms                                                    | 83.1 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                       |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                      |
| regex_effbot   | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                      |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.09 us: 1.05x faster                                      |
| json_loads           | 28.9 us                                                    | 27.9 us: 1.03x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                      |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                       |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                       |
| unpickle             | 15.1 us                                                    | 15.4 us: 1.02x slower                                      |
| pickle_list          | 5.11 us                                                    | 5.28 us: 1.03x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.20 sec: 1.04x slower                                     |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                      |
| Geometric mean       | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.87 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                      |
| genshi_xml     | 51.6 ms                                                    | 52.8 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 112 us: 1.47x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.51 ms: 1.20x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.64 ms: 1.14x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.55 ms: 1.12x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.06 us: 1.10x faster                                      |
| scimark_fft                | 392 ms                                                     | 359 ms: 1.09x faster                                       |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 72.0 ms: 1.08x faster                                      |
| logging_silent             | 105 ns                                                     | 97.7 ns: 1.07x faster                                      |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                     |
| mdp                        | 2.79 sec                                                   | 2.61 sec: 1.07x faster                                     |
| richards_super             | 57.4 ms                                                    | 54.1 ms: 1.06x faster                                      |
| deepcopy                   | 367 us                                                     | 347 us: 1.06x faster                                       |
| richards                   | 50.9 ms                                                    | 48.1 ms: 1.06x faster                                      |
| chameleon                  | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                      |
| unpickle_list              | 5.34 us                                                    | 5.09 us: 1.05x faster                                      |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                       |
| deepcopy_memo              | 39.7 us                                                    | 37.9 us: 1.05x faster                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.05x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.3 ms: 1.04x faster                                      |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                      |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                       |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                       |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.03x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 734 ms: 1.03x faster                                       |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                     |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                       |
| genshi_text                | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                      |
| flaskblogging              | 9.01 ms                                                    | 8.75 ms: 1.03x faster                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.2 ms: 1.03x faster                                      |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.03x faster                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 54.2 ms: 1.02x faster                                      |
| sympy_expand               | 473 ms                                                     | 462 ms: 1.02x faster                                       |
| json                       | 5.31 ms                                                    | 5.19 ms: 1.02x faster                                      |
| pyflate                    | 484 ms                                                     | 474 ms: 1.02x faster                                       |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                       |
| thrift                     | 823 us                                                     | 807 us: 1.02x faster                                       |
| 2to3                       | 274 ms                                                     | 269 ms: 1.02x faster                                       |
| hexiom                     | 6.30 ms                                                    | 6.20 ms: 1.02x faster                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                       |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                       |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                      |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                       |
| nqueens                    | 81.4 ms                                                    | 81.0 ms: 1.01x faster                                      |
| raytrace                   | 267 ms                                                     | 265 ms: 1.01x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.66 ms: 1.00x faster                                      |
| dulwich_log                | 67.2 ms                                                    | 67.0 ms: 1.00x faster                                      |
| fannkuch                   | 402 ms                                                     | 401 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.84 sec: 1.00x faster                                     |
| bench_thread_pool          | 834 us                                                     | 838 us: 1.01x slower                                       |
| logging_format             | 6.47 us                                                    | 6.53 us: 1.01x slower                                      |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                       |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                       |
| logging_simple             | 5.74 us                                                    | 5.83 us: 1.01x slower                                      |
| unpickle                   | 15.1 us                                                    | 15.4 us: 1.02x slower                                      |
| generators                 | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 52.8 ms: 1.02x slower                                      |
| tornado_http               | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                      |
| pickle_list                | 5.11 us                                                    | 5.28 us: 1.03x slower                                      |
| coverage                   | 93.1 ms                                                    | 96.3 ms: 1.03x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.20 sec: 1.04x slower                                     |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                       |
| nbody                      | 88.3 ms                                                    | 92.1 ms: 1.04x slower                                      |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                      |
| float                      | 78.9 ms                                                    | 83.1 ms: 1.05x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.23 sec: 1.06x slower                                     |
| pathlib                    | 17.3 ms                                                    | 18.7 ms: 1.08x slower                                      |
| mypy2                      | 742 ms                                                     | 865 ms: 1.17x slower                                       |
| async_tree_none            | 378 ms                                                     | 444 ms: 1.17x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 718 ms: 1.18x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 571 ms: 1.23x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 733 ms: 1.25x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 8.87 ms: 1.25x slower                                      |
| async_tree_io              | 939 ms                                                     | 1.20 sec: 1.28x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.22 sec: 1.31x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 585 ms: 1.32x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 455 ms: 1.35x slower                                       |
| Geometric mean             | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (15): pylint, xml_etree_parse, xml_etree_generate, aiohttp, deltablue, xml_etree_iterparse, gunicorn, bench_mp_pool, django_template, chaos, mako, pickle_dict, telco, djangocms, html5lib
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x