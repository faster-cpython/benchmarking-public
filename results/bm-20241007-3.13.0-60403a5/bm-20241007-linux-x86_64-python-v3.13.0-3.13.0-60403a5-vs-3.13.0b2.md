# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 265 ms: 1.03x faster                                   |
| chameleon      | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                  |
| docutils       | 2.83 sec                                                   | 2.58 sec: 1.09x faster                                 |
| html5lib       | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                  |
| tornado_http   | 94.6 ms                                                    | 91.5 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                      | 1.05x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 825 ms: 1.13x faster                                   |
| async_tree_io              | 939 ms                                                     | 843 ms: 1.11x faster                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                   |
| async_tree_none            | 378 ms                                                     | 354 ms: 1.07x faster                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                   |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                   |
| async_tree_memoization     | 463 ms                                                     | 442 ms: 1.05x faster                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 465 ms: 1.05x slower                                   |
| Geometric mean             | (ref)                                                      | 1.06x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.7 ms: 1.03x faster                                  |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                   |
| float          | 78.9 ms                                                    | 78.5 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.04x faster                                   |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                   |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                  |
| regex_effbot   | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 4.96 us: 1.08x faster                                  |
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                  |
| xml_etree_iterparse  | 107 ms                                                     | 102 ms: 1.05x faster                                   |
| pickle_dict          | 34.8 us                                                    | 33.2 us: 1.05x faster                                  |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                   |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                  |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                   |
| pickle_list          | 5.11 us                                                    | 5.01 us: 1.02x faster                                  |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                   |
| unpickle             | 15.1 us                                                    | 14.9 us: 1.02x faster                                  |
| xml_etree_process    | 61.2 ms                                                    | 60.4 ms: 1.01x faster                                  |
| xml_etree_generate   | 87.4 ms                                                    | 87.0 ms: 1.01x faster                                  |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                  |
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                  |
| Geometric mean         | (ref)                                                      | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                  |
| genshi_xml      | 51.6 ms                                                    | 50.3 ms: 1.03x faster                                  |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                  |
| django_template | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                      | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 825 ms: 1.13x faster                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.61 ms: 1.13x faster                                  |
| async_tree_io              | 939 ms                                                     | 843 ms: 1.11x faster                                   |
| coverage                   | 93.1 ms                                                    | 83.7 ms: 1.11x faster                                  |
| docutils                   | 2.83 sec                                                   | 2.58 sec: 1.09x faster                                 |
| dask                       | 369 ms                                                     | 338 ms: 1.09x faster                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                   |
| unpickle_list              | 5.34 us                                                    | 4.96 us: 1.08x faster                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.69 sec: 1.07x faster                                 |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                  |
| async_tree_none            | 378 ms                                                     | 354 ms: 1.07x faster                                   |
| dulwich_log                | 67.2 ms                                                    | 63.0 ms: 1.07x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.06x faster                                   |
| scimark_fft                | 392 ms                                                     | 369 ms: 1.06x faster                                   |
| crypto_pyaes               | 77.5 ms                                                    | 73.0 ms: 1.06x faster                                  |
| richards                   | 50.9 ms                                                    | 48.1 ms: 1.06x faster                                  |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                   |
| deepcopy_reduce            | 3.35 us                                                    | 3.17 us: 1.06x faster                                  |
| fannkuch                   | 402 ms                                                     | 381 ms: 1.06x faster                                   |
| richards_super             | 57.4 ms                                                    | 54.4 ms: 1.05x faster                                  |
| chameleon                  | 7.22 ms                                                    | 6.85 ms: 1.05x faster                                  |
| pyflate                    | 484 ms                                                     | 460 ms: 1.05x faster                                   |
| xml_etree_iterparse        | 107 ms                                                     | 102 ms: 1.05x faster                                   |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                   |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                  |
| pickle_dict                | 34.8 us                                                    | 33.2 us: 1.05x faster                                  |
| sqlite_synth               | 2.99 us                                                    | 2.85 us: 1.05x faster                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.03 ms: 1.05x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 442 ms: 1.05x faster                                   |
| deepcopy_memo              | 39.7 us                                                    | 38.0 us: 1.04x faster                                  |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.3 ms: 1.04x faster                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                  |
| regex_compile              | 137 ms                                                     | 131 ms: 1.04x faster                                   |
| deepcopy                   | 367 us                                                     | 352 us: 1.04x faster                                   |
| html5lib                   | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                  |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                   |
| gunicorn                   | 1.28 ms                                                    | 1.23 ms: 1.04x faster                                  |
| asyncio_tcp                | 508 ms                                                     | 488 ms: 1.04x faster                                   |
| scimark_sor                | 127 ms                                                     | 122 ms: 1.04x faster                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                  |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                   |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.03x faster                                   |
| logging_format             | 6.47 us                                                    | 6.25 us: 1.03x faster                                  |
| genshi_text                | 23.7 ms                                                    | 22.9 ms: 1.03x faster                                  |
| 2to3                       | 274 ms                                                     | 265 ms: 1.03x faster                                   |
| tornado_http               | 94.6 ms                                                    | 91.5 ms: 1.03x faster                                  |
| thrift                     | 823 us                                                     | 796 us: 1.03x faster                                   |
| deltablue                  | 3.25 ms                                                    | 3.15 ms: 1.03x faster                                  |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                   |
| aiohttp                    | 1.18 ms                                                    | 1.14 ms: 1.03x faster                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.9 ms: 1.03x faster                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                  |
| coroutines                 | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                  |
| nbody                      | 88.3 ms                                                    | 85.7 ms: 1.03x faster                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                 |
| generators                 | 29.6 ms                                                    | 28.8 ms: 1.03x faster                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                 |
| hexiom                     | 6.30 ms                                                    | 6.13 ms: 1.03x faster                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                   |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                   |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                   |
| genshi_xml                 | 51.6 ms                                                    | 50.3 ms: 1.03x faster                                  |
| sympy_expand               | 473 ms                                                     | 462 ms: 1.02x faster                                   |
| bench_thread_pool          | 834 us                                                     | 815 us: 1.02x faster                                   |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                   |
| go                         | 145 ms                                                     | 142 ms: 1.02x faster                                   |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                   |
| json                       | 5.31 ms                                                    | 5.20 ms: 1.02x faster                                  |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                   |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                   |
| pickle_list                | 5.11 us                                                    | 5.01 us: 1.02x faster                                  |
| raytrace                   | 267 ms                                                     | 262 ms: 1.02x faster                                   |
| pprint_safe_repr           | 758 ms                                                     | 744 ms: 1.02x faster                                   |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                   |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                  |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                  |
| unpickle                   | 15.1 us                                                    | 14.9 us: 1.02x faster                                  |
| mdp                        | 2.79 sec                                                   | 2.74 sec: 1.02x faster                                 |
| pathlib                    | 17.3 ms                                                    | 17.1 ms: 1.02x faster                                  |
| logging_simple             | 5.74 us                                                    | 5.66 us: 1.01x faster                                  |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                  |
| xml_etree_process          | 61.2 ms                                                    | 60.4 ms: 1.01x faster                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                  |
| django_template            | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                  |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                   |
| nqueens                    | 81.4 ms                                                    | 80.6 ms: 1.01x faster                                  |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.01x faster                                   |
| float                      | 78.9 ms                                                    | 78.5 ms: 1.01x faster                                  |
| xml_etree_generate         | 87.4 ms                                                    | 87.0 ms: 1.01x faster                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                  |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                  |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                  |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.03x slower                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 465 ms: 1.05x slower                                   |
| regex_effbot               | 3.67 ms                                                    | 3.88 ms: 1.06x slower                                  |
| mypy2                      | 742 ms                                                     | 1.07 sec: 1.44x slower                                 |
| Geometric mean             | (ref)                                                      | 1.03x faster                                           |

Benchmark hidden because not significant (5): pylint, tomli_loads, telco, flaskblogging, djangocms
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.00x