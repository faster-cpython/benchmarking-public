# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.00x slower
- HPT reliability: 97.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                       |
| chameleon      | 7.22 ms                                                    | 6.87 ms: 1.05x faster                                      |
| docutils       | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                     |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 446 ms: 1.18x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 724 ms: 1.18x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 574 ms: 1.24x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 734 ms: 1.25x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.21 sec: 1.29x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.30x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 586 ms: 1.32x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 447 ms: 1.33x slower                                       |
| Geometric mean             | (ref)                                                      | 1.26x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 191 ms: 1.00x faster                                       |
| nbody          | 88.3 ms                                                    | 89.5 ms: 1.01x slower                                      |
| float          | 78.9 ms                                                    | 82.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                       |
| regex_effbot   | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                      |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                      |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict         | 34.8 us                                                    | 33.8 us: 1.03x faster                                      |
| json_dumps          | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| pickle_list         | 5.11 us                                                    | 4.98 us: 1.02x faster                                      |
| xml_etree_process   | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                      |
| unpickle_list       | 5.34 us                                                    | 5.25 us: 1.02x faster                                      |
| pickle_pure_python  | 305 us                                                     | 302 us: 1.01x faster                                       |
| xml_etree_iterparse | 107 ms                                                     | 106 ms: 1.01x faster                                       |
| tomli_loads         | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                     |
| unpickle            | 15.1 us                                                    | 15.9 us: 1.05x slower                                      |
| Geometric mean      | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (5): xml_etree_parse, json_loads, unpickle_pure_python, xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.92 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                      | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                      |
| mako           | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                      |
| genshi_xml     | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 110 us: 1.50x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.51 ms: 1.20x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                     |
| deepcopy_reduce            | 3.35 us                                                    | 3.11 us: 1.08x faster                                      |
| scimark_fft                | 392 ms                                                     | 366 ms: 1.07x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 72.3 ms: 1.07x faster                                      |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.07x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                     |
| chameleon                  | 7.22 ms                                                    | 6.87 ms: 1.05x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                      |
| deepcopy                   | 367 us                                                     | 350 us: 1.05x faster                                       |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                       |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                       |
| richards_super             | 57.4 ms                                                    | 55.1 ms: 1.04x faster                                      |
| richards                   | 50.9 ms                                                    | 48.9 ms: 1.04x faster                                      |
| coroutines                 | 23.2 ms                                                    | 22.3 ms: 1.04x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.04x faster                                      |
| sqlite_synth               | 2.99 us                                                    | 2.88 us: 1.04x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 38.4 us: 1.03x faster                                      |
| thrift                     | 823 us                                                     | 796 us: 1.03x faster                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                      |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.10 ms: 1.03x faster                                      |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                      |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                       |
| pickle_dict                | 34.8 us                                                    | 33.8 us: 1.03x faster                                      |
| sympy_str                  | 282 ms                                                     | 275 ms: 1.03x faster                                       |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.03x faster                                      |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                       |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                       |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                      |
| flaskblogging              | 9.01 ms                                                    | 8.79 ms: 1.03x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.98 us: 1.02x faster                                      |
| chaos                      | 61.3 ms                                                    | 59.9 ms: 1.02x faster                                      |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                      |
| genshi_text                | 23.7 ms                                                    | 23.2 ms: 1.02x faster                                      |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 745 ms: 1.02x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                      |
| generators                 | 29.6 ms                                                    | 29.2 ms: 1.02x faster                                      |
| sympy_expand               | 473 ms                                                     | 466 ms: 1.02x faster                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.53 sec: 1.01x faster                                     |
| 2to3                       | 274 ms                                                     | 270 ms: 1.01x faster                                       |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                       |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                       |
| nqueens                    | 81.4 ms                                                    | 80.7 ms: 1.01x faster                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.6 ms: 1.01x faster                                      |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                       |
| aiohttp                    | 1.18 ms                                                    | 1.17 ms: 1.01x faster                                      |
| gunicorn                   | 1.28 ms                                                    | 1.27 ms: 1.01x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                     |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                       |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                      |
| dulwich_log                | 67.2 ms                                                    | 66.8 ms: 1.01x faster                                      |
| pidigits                   | 191 ms                                                     | 191 ms: 1.00x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.68 ms: 1.00x slower                                      |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.00x slower                                      |
| logging_silent             | 105 ns                                                     | 105 ns: 1.00x slower                                       |
| logging_format             | 6.47 us                                                    | 6.53 us: 1.01x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| bench_thread_pool          | 834 us                                                     | 842 us: 1.01x slower                                       |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                      |
| nbody                      | 88.3 ms                                                    | 89.5 ms: 1.01x slower                                      |
| json                       | 5.31 ms                                                    | 5.39 ms: 1.02x slower                                      |
| telco                      | 8.41 ms                                                    | 8.55 ms: 1.02x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                     |
| tornado_http               | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                      |
| logging_simple             | 5.74 us                                                    | 5.89 us: 1.02x slower                                      |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                       |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                       |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                     |
| coverage                   | 93.1 ms                                                    | 95.8 ms: 1.03x slower                                      |
| float                      | 78.9 ms                                                    | 82.0 ms: 1.04x slower                                      |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                       |
| unpickle                   | 15.1 us                                                    | 15.9 us: 1.05x slower                                      |
| pathlib                    | 17.3 ms                                                    | 18.5 ms: 1.07x slower                                      |
| mypy2                      | 742 ms                                                     | 865 ms: 1.17x slower                                       |
| async_tree_none            | 378 ms                                                     | 446 ms: 1.18x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 724 ms: 1.18x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 574 ms: 1.24x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 734 ms: 1.25x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 8.92 ms: 1.26x slower                                      |
| async_tree_io              | 939 ms                                                     | 1.21 sec: 1.29x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.21 sec: 1.30x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 586 ms: 1.32x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 447 ms: 1.33x slower                                       |
| Geometric mean             | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (12): pylint, xml_etree_parse, json_loads, django_template, bench_mp_pool, meteor_contest, unpickle_pure_python, xml_etree_generate, fannkuch, pickle, djangocms, html5lib
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 97.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.95x