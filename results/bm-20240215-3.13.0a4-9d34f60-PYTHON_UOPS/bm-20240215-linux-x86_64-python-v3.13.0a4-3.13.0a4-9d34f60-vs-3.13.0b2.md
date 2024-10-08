# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x slower
- HPT reliability: 94.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                       |
| chameleon      | 7.22 ms                                                    | 6.93 ms: 1.04x faster                                      |
| docutils       | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| tornado_http   | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 438 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 710 ms: 1.16x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 565 ms: 1.22x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 723 ms: 1.23x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.26x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.20 sec: 1.29x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 576 ms: 1.30x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 448 ms: 1.33x slower                                       |
| Geometric mean             | (ref)                                                      | 1.24x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| float          | 78.9 ms                                                    | 85.3 ms: 1.08x slower                                      |
| nbody          | 88.3 ms                                                    | 103 ms: 1.17x slower                                       |
| Geometric mean | (ref)                                                      | 1.08x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                      |
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                       |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 4.96 us: 1.08x faster                                      |
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                      |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.02x faster                                       |
| pickle_list          | 5.11 us                                                    | 5.00 us: 1.02x faster                                      |
| xml_etree_generate   | 87.4 ms                                                    | 86.0 ms: 1.02x faster                                      |
| pickle_dict          | 34.8 us                                                    | 34.2 us: 1.02x faster                                      |
| pickle               | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| unpickle             | 15.1 us                                                    | 15.3 us: 1.01x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.21 sec: 1.04x slower                                     |
| unpickle_pure_python | 218 us                                                     | 230 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.2 ms: 1.05x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.84 ms: 1.24x slower                                      |
| Geometric mean         | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                      |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                      |
| genshi_xml      | 51.6 ms                                                    | 52.7 ms: 1.02x slower                                      |
| mako            | 11.2 ms                                                    | 12.1 ms: 1.07x slower                                      |
| Geometric mean  | (ref)                                                      | 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 111 us: 1.48x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.48 ms: 1.23x faster                                      |
| richards                   | 50.9 ms                                                    | 45.3 ms: 1.12x faster                                      |
| richards_super             | 57.4 ms                                                    | 51.7 ms: 1.11x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.03 us: 1.10x faster                                      |
| unpickle_list              | 5.34 us                                                    | 4.96 us: 1.08x faster                                      |
| docutils                   | 2.83 sec                                                   | 2.64 sec: 1.07x faster                                     |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                      |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 478 ms: 1.06x faster                                       |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                      |
| python_startup             | 10.8 ms                                                    | 10.2 ms: 1.05x faster                                      |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                      |
| deepcopy                   | 367 us                                                     | 350 us: 1.05x faster                                       |
| xml_etree_process          | 61.2 ms                                                    | 58.4 ms: 1.05x faster                                      |
| json                       | 5.31 ms                                                    | 5.07 ms: 1.05x faster                                      |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                       |
| scimark_lu                 | 122 ms                                                     | 117 ms: 1.04x faster                                       |
| chameleon                  | 7.22 ms                                                    | 6.93 ms: 1.04x faster                                      |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                       |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                       |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 38.5 us: 1.03x faster                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                     |
| mdp                        | 2.79 sec                                                   | 2.71 sec: 1.03x faster                                     |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 553 ms: 1.03x faster                                       |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.02x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                      |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                       |
| pickle_list                | 5.11 us                                                    | 5.00 us: 1.02x faster                                      |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                       |
| xml_etree_generate         | 87.4 ms                                                    | 86.0 ms: 1.02x faster                                      |
| pickle_dict                | 34.8 us                                                    | 34.2 us: 1.02x faster                                      |
| generators                 | 29.6 ms                                                    | 29.2 ms: 1.02x faster                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                      |
| genshi_text                | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                       |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.01x faster                                      |
| gunicorn                   | 1.28 ms                                                    | 1.27 ms: 1.01x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 20.6 ms: 1.00x slower                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| bench_thread_pool          | 834 us                                                     | 839 us: 1.01x slower                                       |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                       |
| unpickle                   | 15.1 us                                                    | 15.3 us: 1.01x slower                                      |
| logging_simple             | 5.74 us                                                    | 5.81 us: 1.01x slower                                      |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                       |
| crypto_pyaes               | 77.5 ms                                                    | 78.6 ms: 1.01x slower                                      |
| pprint_safe_repr           | 758 ms                                                     | 770 ms: 1.02x slower                                       |
| coverage                   | 93.1 ms                                                    | 94.7 ms: 1.02x slower                                      |
| sympy_sum                  | 156 ms                                                     | 159 ms: 1.02x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 52.7 ms: 1.02x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                     |
| dulwich_log                | 67.2 ms                                                    | 68.7 ms: 1.02x slower                                      |
| tornado_http               | 94.6 ms                                                    | 96.9 ms: 1.02x slower                                      |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                       |
| sympy_expand               | 473 ms                                                     | 484 ms: 1.02x slower                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 5.15 sec: 1.03x slower                                     |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                       |
| deltablue                  | 3.25 ms                                                    | 3.37 ms: 1.04x slower                                      |
| flaskblogging              | 9.01 ms                                                    | 9.37 ms: 1.04x slower                                      |
| djangocms                  | 31.5 us                                                    | 32.8 us: 1.04x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.21 sec: 1.04x slower                                     |
| raytrace                   | 267 ms                                                     | 279 ms: 1.04x slower                                       |
| fannkuch                   | 402 ms                                                     | 420 ms: 1.05x slower                                       |
| pyflate                    | 484 ms                                                     | 507 ms: 1.05x slower                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.63 sec: 1.05x slower                                     |
| unpickle_pure_python       | 218 us                                                     | 230 us: 1.05x slower                                       |
| pathlib                    | 17.3 ms                                                    | 18.4 ms: 1.06x slower                                      |
| mako                       | 11.2 ms                                                    | 12.1 ms: 1.07x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 74.5 ms: 1.08x slower                                      |
| float                      | 78.9 ms                                                    | 85.3 ms: 1.08x slower                                      |
| comprehensions             | 16.6 us                                                    | 18.3 us: 1.10x slower                                      |
| nqueens                    | 81.4 ms                                                    | 91.0 ms: 1.12x slower                                      |
| chaos                      | 61.3 ms                                                    | 69.5 ms: 1.13x slower                                      |
| spectral_norm              | 116 ms                                                     | 132 ms: 1.14x slower                                       |
| async_tree_none            | 378 ms                                                     | 438 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 710 ms: 1.16x slower                                       |
| mypy2                      | 742 ms                                                     | 865 ms: 1.17x slower                                       |
| nbody                      | 88.3 ms                                                    | 103 ms: 1.17x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 565 ms: 1.22x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 723 ms: 1.23x slower                                       |
| hexiom                     | 6.30 ms                                                    | 7.76 ms: 1.23x slower                                      |
| python_startup_no_site     | 7.11 ms                                                    | 8.84 ms: 1.24x slower                                      |
| async_tree_io              | 939 ms                                                     | 1.18 sec: 1.26x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.20 sec: 1.29x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 576 ms: 1.30x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 448 ms: 1.33x slower                                       |
| Geometric mean             | (ref)                                                      | 1.02x slower                                               |

Benchmark hidden because not significant (10): pylint, xml_etree_iterparse, aiohttp, logging_format, telco, html5lib, sympy_str, sqlglot_optimize, regex_v8, scimark_sparse_mat_mult
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dask
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: unpack_sequence

# HPT report

- Reliability score: 94.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x