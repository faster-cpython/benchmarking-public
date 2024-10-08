# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 263 ms: 1.04x faster                                         |
| chameleon      | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                        |
| docutils       | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                       |
| html5lib       | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                        |
| tornado_http   | 94.6 ms                                                    | 91.4 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                      | 1.04x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 889 ms: 1.06x faster                                         |
| async_tree_none            | 378 ms                                                     | 362 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 564 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 588 ms: 1.04x faster                                         |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                 |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                         |
| float          | 78.9 ms                                                    | 77.4 ms: 1.02x faster                                        |
| nbody          | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                        |
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                        |
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                         |
| regex_dna      | 221 ms                                                     | 216 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                      | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads         | 28.9 us                                                    | 27.1 us: 1.07x faster                                        |
| unpickle_list      | 5.34 us                                                    | 5.06 us: 1.06x faster                                        |
| xml_etree_parse    | 162 ms                                                     | 156 ms: 1.04x faster                                         |
| json_dumps         | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                        |
| tomli_loads        | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                       |
| unpickle           | 15.1 us                                                    | 14.9 us: 1.01x faster                                        |
| pickle_pure_python | 305 us                                                     | 302 us: 1.01x faster                                         |
| pickle_dict        | 34.8 us                                                    | 34.5 us: 1.01x faster                                        |
| xml_etree_process  | 61.2 ms                                                    | 60.8 ms: 1.01x faster                                        |
| pickle_list        | 5.11 us                                                    | 5.25 us: 1.03x slower                                        |
| Geometric mean     | (ref)                                                      | 1.02x faster                                                 |

Benchmark hidden because not significant (4): pickle, xml_etree_iterparse, unpickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 6.96 ms: 1.02x faster                                        |
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                        |
| genshi_xml      | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                        |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                        |
| mako            | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------:|
| coverage                   | 93.1 ms                                                    | 84.1 ms: 1.11x faster                                        |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                         |
| richards_super             | 57.4 ms                                                    | 53.2 ms: 1.08x faster                                        |
| richards                   | 50.9 ms                                                    | 47.3 ms: 1.08x faster                                        |
| scimark_fft                | 392 ms                                                     | 365 ms: 1.08x faster                                         |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                        |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.06x faster                                        |
| asyncio_tcp                | 508 ms                                                     | 480 ms: 1.06x faster                                         |
| async_tree_io              | 939 ms                                                     | 889 ms: 1.06x faster                                         |
| unpickle_list              | 5.34 us                                                    | 5.06 us: 1.06x faster                                        |
| dulwich_log                | 67.2 ms                                                    | 63.7 ms: 1.05x faster                                        |
| regex_effbot               | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.01 ms: 1.05x faster                                        |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                        |
| coroutines                 | 23.2 ms                                                    | 22.1 ms: 1.05x faster                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                       |
| async_tree_none            | 378 ms                                                     | 362 ms: 1.04x faster                                         |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 564 ms: 1.04x faster                                         |
| 2to3                       | 274 ms                                                     | 263 ms: 1.04x faster                                         |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                        |
| deepcopy_reduce            | 3.35 us                                                    | 3.22 us: 1.04x faster                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 588 ms: 1.04x faster                                         |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                         |
| pyflate                    | 484 ms                                                     | 467 ms: 1.04x faster                                         |
| chameleon                  | 7.22 ms                                                    | 6.97 ms: 1.04x faster                                        |
| html5lib                   | 67.2 ms                                                    | 64.9 ms: 1.04x faster                                        |
| tornado_http               | 94.6 ms                                                    | 91.4 ms: 1.04x faster                                        |
| mypy2                      | 742 ms                                                     | 717 ms: 1.04x faster                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.78 sec: 1.03x faster                                       |
| gunicorn                   | 1.28 ms                                                    | 1.24 ms: 1.03x faster                                        |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                        |
| nqueens                    | 81.4 ms                                                    | 78.9 ms: 1.03x faster                                        |
| aiohttp                    | 1.18 ms                                                    | 1.14 ms: 1.03x faster                                        |
| dask                       | 369 ms                                                     | 358 ms: 1.03x faster                                         |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                         |
| docutils                   | 2.83 sec                                                   | 2.74 sec: 1.03x faster                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                        |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                         |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                        |
| crypto_pyaes               | 77.5 ms                                                    | 75.3 ms: 1.03x faster                                        |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                        |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                         |
| sympy_str                  | 282 ms                                                     | 275 ms: 1.03x faster                                         |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                         |
| django_template            | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                        |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                       |
| logging_silent             | 105 ns                                                     | 102 ns: 1.02x faster                                         |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                        |
| deepcopy                   | 367 us                                                     | 359 us: 1.02x faster                                         |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                       |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.02x faster                                         |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                         |
| thrift                     | 823 us                                                     | 806 us: 1.02x faster                                         |
| python_startup_no_site     | 7.11 ms                                                    | 6.96 ms: 1.02x faster                                        |
| pprint_safe_repr           | 758 ms                                                     | 744 ms: 1.02x faster                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                        |
| generators                 | 29.6 ms                                                    | 29.1 ms: 1.02x faster                                        |
| bench_thread_pool          | 834 us                                                     | 818 us: 1.02x faster                                         |
| float                      | 78.9 ms                                                    | 77.4 ms: 1.02x faster                                        |
| sympy_expand               | 473 ms                                                     | 464 ms: 1.02x faster                                         |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                         |
| async_generators           | 442 ms                                                     | 435 ms: 1.02x faster                                         |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.02x faster                                       |
| genshi_xml                 | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                        |
| scimark_monte_carlo        | 69.2 ms                                                    | 68.2 ms: 1.01x faster                                        |
| sqlglot_normalize          | 110 ms                                                     | 109 ms: 1.01x faster                                         |
| logging_format             | 6.47 us                                                    | 6.39 us: 1.01x faster                                        |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.01x faster                                       |
| json                       | 5.31 ms                                                    | 5.24 ms: 1.01x faster                                        |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.01x faster                                        |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                         |
| genshi_text                | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                        |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                         |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                        |
| fannkuch                   | 402 ms                                                     | 398 ms: 1.01x faster                                         |
| pickle_dict                | 34.8 us                                                    | 34.5 us: 1.01x faster                                        |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                         |
| logging_simple             | 5.74 us                                                    | 5.70 us: 1.01x faster                                        |
| pathlib                    | 17.3 ms                                                    | 17.2 ms: 1.01x faster                                        |
| xml_etree_process          | 61.2 ms                                                    | 60.8 ms: 1.01x faster                                        |
| deepcopy_memo              | 39.7 us                                                    | 39.5 us: 1.01x faster                                        |
| nbody                      | 88.3 ms                                                    | 88.0 ms: 1.00x faster                                        |
| raytrace                   | 267 ms                                                     | 267 ms: 1.00x slower                                         |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                        |
| mako                       | 11.2 ms                                                    | 11.4 ms: 1.01x slower                                        |
| flaskblogging              | 9.01 ms                                                    | 9.16 ms: 1.02x slower                                        |
| telco                      | 8.41 ms                                                    | 8.63 ms: 1.03x slower                                        |
| pickle_list                | 5.11 us                                                    | 5.25 us: 1.03x slower                                        |
| djangocms                  | 31.5 us                                                    | 32.5 us: 1.03x slower                                        |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                 |

Benchmark hidden because not significant (12): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, pickle, deltablue, xml_etree_iterparse, async_tree_none_tg, hexiom, unpickle_pure_python, xml_etree_generate, spectral_norm, pylint
Ignored benchmarks (1) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x