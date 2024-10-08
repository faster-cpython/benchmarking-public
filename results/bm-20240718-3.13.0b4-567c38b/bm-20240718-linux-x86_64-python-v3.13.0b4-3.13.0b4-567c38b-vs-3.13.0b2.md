# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 265 ms: 1.03x faster                                       |
| chameleon      | 7.22 ms                                                    | 6.96 ms: 1.04x faster                                      |
| docutils       | 2.83 sec                                                   | 2.75 sec: 1.03x faster                                     |
| tornado_http   | 94.6 ms                                                    | 91.7 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 429 ms: 1.03x faster                                       |
| async_tree_none            | 378 ms                                                     | 366 ms: 1.03x faster                                       |
| async_tree_none_tg         | 336 ms                                                     | 325 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                       |
| Geometric mean             | (ref)                                                      | 1.03x faster                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.6 ms: 1.03x faster                                      |
| float          | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                      | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                       |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                      |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.9 us: 1.03x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 158 ms: 1.02x faster                                       |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                       |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                       |
| xml_etree_process    | 61.2 ms                                                    | 60.9 ms: 1.00x faster                                      |
| tomli_loads          | 2.12 sec                                                   | 2.13 sec: 1.01x slower                                     |
| Geometric mean       | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                      |
| Geometric mean         | (ref)                                                      | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                      |
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                      |
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                      |
| genshi_xml      | 51.6 ms                                                    | 50.7 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                      | 1.02x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                      |
| scimark_fft                | 392 ms                                                     | 370 ms: 1.06x faster                                       |
| richards                   | 50.9 ms                                                    | 48.0 ms: 1.06x faster                                      |
| json                       | 5.31 ms                                                    | 5.01 ms: 1.06x faster                                      |
| richards_super             | 57.4 ms                                                    | 54.2 ms: 1.06x faster                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                     |
| dulwich_log                | 67.2 ms                                                    | 63.7 ms: 1.05x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.01 ms: 1.05x faster                                      |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                       |
| scimark_lu                 | 122 ms                                                     | 116 ms: 1.05x faster                                       |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.05x faster                                     |
| deepcopy_reduce            | 3.35 us                                                    | 3.21 us: 1.04x faster                                      |
| async_tree_io              | 939 ms                                                     | 902 ms: 1.04x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 74.4 ms: 1.04x faster                                      |
| async_tree_io_tg           | 936 ms                                                     | 901 ms: 1.04x faster                                       |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                       |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.04x faster                                       |
| logging_format             | 6.47 us                                                    | 6.23 us: 1.04x faster                                      |
| chameleon                  | 7.22 ms                                                    | 6.96 ms: 1.04x faster                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 429 ms: 1.03x faster                                       |
| 2to3                       | 274 ms                                                     | 265 ms: 1.03x faster                                       |
| json_loads                 | 28.9 us                                                    | 27.9 us: 1.03x faster                                      |
| mypy2                      | 742 ms                                                     | 717 ms: 1.03x faster                                       |
| async_tree_none            | 378 ms                                                     | 366 ms: 1.03x faster                                       |
| async_tree_none_tg         | 336 ms                                                     | 325 ms: 1.03x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 492 ms: 1.03x faster                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 53.7 ms: 1.03x faster                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 38.5 us: 1.03x faster                                      |
| nqueens                    | 81.4 ms                                                    | 78.9 ms: 1.03x faster                                      |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                       |
| tornado_http               | 94.6 ms                                                    | 91.7 ms: 1.03x faster                                      |
| chaos                      | 61.3 ms                                                    | 59.5 ms: 1.03x faster                                      |
| nbody                      | 88.3 ms                                                    | 85.6 ms: 1.03x faster                                      |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 570 ms: 1.03x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.75 sec: 1.03x faster                                     |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                       |
| hexiom                     | 6.30 ms                                                    | 6.12 ms: 1.03x faster                                      |
| deepcopy                   | 367 us                                                     | 357 us: 1.03x faster                                       |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                      |
| sympy_expand               | 473 ms                                                     | 460 ms: 1.03x faster                                       |
| generators                 | 29.6 ms                                                    | 28.8 ms: 1.03x faster                                      |
| float                      | 78.9 ms                                                    | 76.8 ms: 1.03x faster                                      |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                       |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                      |
| xml_etree_parse            | 162 ms                                                     | 158 ms: 1.02x faster                                       |
| async_generators           | 442 ms                                                     | 432 ms: 1.02x faster                                       |
| bench_thread_pool          | 834 us                                                     | 814 us: 1.02x faster                                       |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                       |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                      |
| mako                       | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                      |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                      |
| django_template            | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                      |
| pathlib                    | 17.3 ms                                                    | 17.0 ms: 1.02x faster                                      |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                      |
| logging_simple             | 5.74 us                                                    | 5.64 us: 1.02x faster                                      |
| genshi_xml                 | 51.6 ms                                                    | 50.7 ms: 1.02x faster                                      |
| coverage                   | 93.1 ms                                                    | 91.7 ms: 1.02x faster                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.01x faster                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.96 sec: 1.01x faster                                     |
| raytrace                   | 267 ms                                                     | 264 ms: 1.01x faster                                       |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                       |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                       |
| telco                      | 8.41 ms                                                    | 8.34 ms: 1.01x faster                                      |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                       |
| pyflate                    | 484 ms                                                     | 481 ms: 1.01x faster                                       |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                      |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                       |
| xml_etree_process          | 61.2 ms                                                    | 60.9 ms: 1.00x faster                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                      |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.13 sec: 1.01x slower                                     |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                     |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                      |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                       |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                       |
| Geometric mean             | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (9): pylint, async_tree_cpu_io_mixed, async_tree_memoization, html5lib, deltablue, xml_etree_generate, scimark_monte_carlo, fannkuch, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x