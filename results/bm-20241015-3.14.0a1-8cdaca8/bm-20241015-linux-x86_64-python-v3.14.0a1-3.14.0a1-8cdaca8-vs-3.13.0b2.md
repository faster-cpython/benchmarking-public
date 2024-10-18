# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                       |
| docutils       | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                     |
| html5lib       | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                      |
| tornado_http   | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                      | 1.07x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                       |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                       |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                       |
| async_tree_none_tg         | 336 ms                                                     | 322 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 562 ms: 1.05x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 968 ms: 1.03x slower                                       |
| Geometric mean             | (ref)                                                      | 1.08x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| nbody          | 88.3 ms                                                    | 88.8 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 129 ms: 1.06x faster                                       |
| regex_dna      | 221 ms                                                     | 214 ms: 1.03x faster                                       |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                      |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                      |
| pickle_dict          | 34.8 us                                                    | 33.3 us: 1.05x faster                                      |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                       |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| tomli_loads          | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                     |
| xml_etree_process    | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| unpickle             | 15.1 us                                                    | 15.0 us: 1.01x faster                                      |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                       |
| pickle_pure_python   | 305 us                                                     | 313 us: 1.02x slower                                       |
| unpickle_list        | 5.34 us                                                    | 5.49 us: 1.03x slower                                      |
| json_dumps           | 10.7 ms                                                    | 11.1 ms: 1.03x slower                                      |
| Geometric mean       | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (3): pickle_list, xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                      |
| python_startup         | 10.8 ms                                                    | 11.8 ms: 1.10x slower                                      |
| Geometric mean         | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                      |
| genshi_text     | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                      |
| genshi_xml      | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                       |
| deepcopy_memo              | 39.7 us                                                    | 30.4 us: 1.31x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                      |
| go                         | 145 ms                                                     | 120 ms: 1.20x faster                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                       |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                       |
| async_tree_memoization     | 463 ms                                                     | 415 ms: 1.12x faster                                       |
| coverage                   | 93.1 ms                                                    | 83.6 ms: 1.11x faster                                      |
| richards                   | 50.9 ms                                                    | 46.0 ms: 1.11x faster                                      |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.79 ms: 1.10x faster                                      |
| generators                 | 29.6 ms                                                    | 27.0 ms: 1.10x faster                                      |
| scimark_fft                | 392 ms                                                     | 360 ms: 1.09x faster                                       |
| richards_super             | 57.4 ms                                                    | 52.8 ms: 1.09x faster                                      |
| html5lib                   | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                      |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                       |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                      |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 72.1 ms: 1.07x faster                                      |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                      |
| sympy_sum                  | 156 ms                                                     | 146 ms: 1.07x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.65 sec: 1.07x faster                                     |
| thrift                     | 823 us                                                     | 773 us: 1.06x faster                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 575 ms: 1.06x faster                                       |
| sympy_str                  | 282 ms                                                     | 266 ms: 1.06x faster                                       |
| regex_compile              | 137 ms                                                     | 129 ms: 1.06x faster                                       |
| dulwich_log                | 67.2 ms                                                    | 63.5 ms: 1.06x faster                                      |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                      |
| json                       | 5.31 ms                                                    | 5.03 ms: 1.06x faster                                      |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.06x faster                                      |
| tornado_http               | 94.6 ms                                                    | 89.9 ms: 1.05x faster                                      |
| sympy_expand               | 473 ms                                                     | 450 ms: 1.05x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                     |
| asyncio_tcp                | 508 ms                                                     | 486 ms: 1.05x faster                                       |
| logging_silent             | 105 ns                                                     | 100 ns: 1.05x faster                                       |
| pickle_dict                | 34.8 us                                                    | 33.3 us: 1.05x faster                                      |
| async_tree_none_tg         | 336 ms                                                     | 322 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 562 ms: 1.05x faster                                       |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.04x faster                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                      |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 106 ms: 1.04x faster                                       |
| pprint_safe_repr           | 758 ms                                                     | 734 ms: 1.03x faster                                       |
| sympy_integrate            | 20.5 ms                                                    | 19.8 ms: 1.03x faster                                      |
| regex_dna                  | 221 ms                                                     | 214 ms: 1.03x faster                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                     |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                     |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                     |
| pyflate                    | 484 ms                                                     | 471 ms: 1.03x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.4 ms: 1.03x faster                                      |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                       |
| django_template            | 34.8 ms                                                    | 34.0 ms: 1.02x faster                                      |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                       |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                      |
| chaos                      | 61.3 ms                                                    | 60.1 ms: 1.02x faster                                      |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                       |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                       |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                      |
| nqueens                    | 81.4 ms                                                    | 79.9 ms: 1.02x faster                                      |
| hexiom                     | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                      |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                       |
| tomli_loads                | 2.12 sec                                                   | 2.09 sec: 1.01x faster                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 60.5 ms: 1.01x faster                                      |
| genshi_text                | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                      |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                      |
| unpickle                   | 15.1 us                                                    | 15.0 us: 1.01x faster                                      |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                       |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.00x slower                                      |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                       |
| fannkuch                   | 402 ms                                                     | 404 ms: 1.01x slower                                       |
| nbody                      | 88.3 ms                                                    | 88.8 ms: 1.01x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 52.1 ms: 1.01x slower                                      |
| async_generators           | 442 ms                                                     | 447 ms: 1.01x slower                                       |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                      |
| pickle_pure_python         | 305 us                                                     | 313 us: 1.02x slower                                       |
| unpickle_list              | 5.34 us                                                    | 5.49 us: 1.03x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 11.1 ms: 1.03x slower                                      |
| async_tree_io_tg           | 936 ms                                                     | 968 ms: 1.03x slower                                       |
| python_startup             | 10.8 ms                                                    | 11.8 ms: 1.10x slower                                      |
| gc_traversal               | 3.98 ms                                                    | 4.54 ms: 1.14x slower                                      |
| create_gc_cycles           | 1.82 ms                                                    | 2.67 ms: 1.47x slower                                      |
| bench_mp_pool              | 23.9 ms                                                    | 77.9 ms: 3.26x slower                                      |
| Geometric mean             | (ref)                                                      | 1.03x faster                                               |

Benchmark hidden because not significant (7): coroutines, pickle_list, pylint, xml_etree_generate, mako, pickle, float
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x