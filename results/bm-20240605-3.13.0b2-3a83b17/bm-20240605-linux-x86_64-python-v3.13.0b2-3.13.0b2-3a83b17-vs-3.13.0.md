# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.03x slower                                       |
| chameleon      | 6.85 ms                                                | 7.22 ms: 1.05x slower                                      |
| docutils       | 2.58 sec                                               | 2.83 sec: 1.09x slower                                     |
| html5lib       | 64.5 ms                                                | 67.2 ms: 1.04x slower                                      |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 444 ms: 1.05x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 508 ms: 1.04x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 463 ms: 1.05x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 336 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 611 ms: 1.06x slower                                       |
| async_tree_none            | 354 ms                                                 | 378 ms: 1.07x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 587 ms: 1.08x slower                                       |
| async_tree_io              | 843 ms                                                 | 939 ms: 1.11x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 936 ms: 1.13x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.9 ms: 1.01x slower                                      |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                       |
| nbody          | 85.7 ms                                                | 88.3 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                       |
| regex_compile  | 131 ms                                                 | 137 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| xml_etree_generate   | 87.0 ms                                                | 87.4 ms: 1.01x slower                                      |
| xml_etree_process    | 60.4 ms                                                | 61.2 ms: 1.01x slower                                      |
| unpickle             | 14.9 us                                                | 15.1 us: 1.02x slower                                      |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                       |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                      |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                       |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| json_loads           | 27.0 us                                                | 28.9 us: 1.07x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.34 us: 1.08x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.11 ms: 1.02x slower                                      |
| python_startup         | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.8 ms: 1.01x slower                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| genshi_xml      | 50.3 ms                                                | 51.6 ms: 1.03x slower                                      |
| genshi_text     | 22.9 ms                                                | 23.7 ms: 1.03x slower                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 742 ms: 1.44x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 444 ms: 1.05x faster                                       |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                     |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.4 ms: 1.01x slower                                      |
| float                      | 78.5 ms                                                | 78.9 ms: 1.01x slower                                      |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                       |
| nqueens                    | 80.6 ms                                                | 81.4 ms: 1.01x slower                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| django_template            | 34.4 ms                                                | 34.8 ms: 1.01x slower                                      |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| xml_etree_process          | 60.4 ms                                                | 61.2 ms: 1.01x slower                                      |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                      |
| logging_simple             | 5.66 us                                                | 5.74 us: 1.01x slower                                      |
| pathlib                    | 17.1 ms                                                | 17.3 ms: 1.02x slower                                      |
| mdp                        | 2.74 sec                                               | 2.79 sec: 1.02x slower                                     |
| unpickle                   | 14.9 us                                                | 15.1 us: 1.02x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.11 ms: 1.02x slower                                      |
| python_startup             | 10.6 ms                                                | 10.8 ms: 1.02x slower                                      |
| pickle_pure_python         | 300 us                                                 | 305 us: 1.02x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 758 ms: 1.02x slower                                       |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                       |
| pickle_list                | 5.01 us                                                | 5.11 us: 1.02x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 567 ms: 1.02x slower                                       |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| json                       | 5.20 ms                                                | 5.31 ms: 1.02x slower                                      |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                       |
| go                         | 142 ms                                                 | 145 ms: 1.02x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                       |
| bench_thread_pool          | 815 us                                                 | 834 us: 1.02x slower                                       |
| sympy_expand               | 462 ms                                                 | 473 ms: 1.02x slower                                       |
| genshi_xml                 | 50.3 ms                                                | 51.6 ms: 1.03x slower                                      |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                       |
| sqlglot_normalize          | 107 ms                                                 | 110 ms: 1.03x slower                                       |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                       |
| hexiom                     | 6.13 ms                                                | 6.30 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                     |
| nbody                      | 85.7 ms                                                | 88.3 ms: 1.03x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 55.5 ms: 1.03x slower                                      |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.5 ms: 1.03x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.18 ms: 1.03x slower                                      |
| sympy_str                  | 274 ms                                                 | 282 ms: 1.03x slower                                       |
| deltablue                  | 3.15 ms                                                | 3.25 ms: 1.03x slower                                      |
| thrift                     | 796 us                                                 | 823 us: 1.03x slower                                       |
| tornado_http               | 91.5 ms                                                | 94.6 ms: 1.03x slower                                      |
| 2to3                       | 265 ms                                                 | 274 ms: 1.03x slower                                       |
| genshi_text                | 22.9 ms                                                | 23.7 ms: 1.03x slower                                      |
| logging_format             | 6.25 us                                                | 6.47 us: 1.03x slower                                      |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.03x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 162 ms: 1.04x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                      |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 508 ms: 1.04x slower                                       |
| gunicorn                   | 1.23 ms                                                | 1.28 ms: 1.04x slower                                      |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                       |
| html5lib                   | 64.5 ms                                                | 67.2 ms: 1.04x slower                                      |
| deepcopy                   | 352 us                                                 | 367 us: 1.04x slower                                       |
| regex_compile              | 131 ms                                                 | 137 ms: 1.04x slower                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 69.2 ms: 1.04x slower                                      |
| gc_traversal               | 3.81 ms                                                | 3.98 ms: 1.04x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 39.7 us: 1.04x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 463 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.27 ms: 1.05x slower                                      |
| sqlite_synth               | 2.85 us                                                | 2.99 us: 1.05x slower                                      |
| pickle_dict                | 33.2 us                                                | 34.8 us: 1.05x slower                                      |
| chaos                      | 58.4 ms                                                | 61.3 ms: 1.05x slower                                      |
| async_tree_none_tg         | 320 ms                                                 | 336 ms: 1.05x slower                                       |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                       |
| pyflate                    | 460 ms                                                 | 484 ms: 1.05x slower                                       |
| chameleon                  | 6.85 ms                                                | 7.22 ms: 1.05x slower                                      |
| richards_super             | 54.4 ms                                                | 57.4 ms: 1.05x slower                                      |
| fannkuch                   | 381 ms                                                 | 402 ms: 1.06x slower                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.35 us: 1.06x slower                                      |
| scimark_lu                 | 115 ms                                                 | 122 ms: 1.06x slower                                       |
| richards                   | 48.1 ms                                                | 50.9 ms: 1.06x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 77.5 ms: 1.06x slower                                      |
| scimark_fft                | 369 ms                                                 | 392 ms: 1.06x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 611 ms: 1.06x slower                                       |
| dulwich_log                | 63.0 ms                                                | 67.2 ms: 1.07x slower                                      |
| async_tree_none            | 354 ms                                                 | 378 ms: 1.07x slower                                       |
| json_loads                 | 27.0 us                                                | 28.9 us: 1.07x slower                                      |
| bpe_tokeniser              | 4.69 sec                                               | 5.02 sec: 1.07x slower                                     |
| unpickle_list              | 4.96 us                                                | 5.34 us: 1.08x slower                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 587 ms: 1.08x slower                                       |
| dask                       | 338 ms                                                 | 369 ms: 1.09x slower                                       |
| docutils                   | 2.58 sec                                               | 2.83 sec: 1.09x slower                                     |
| coverage                   | 83.7 ms                                                | 93.1 ms: 1.11x slower                                      |
| async_tree_io              | 843 ms                                                 | 939 ms: 1.11x slower                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.82 ms: 1.13x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 936 ms: 1.13x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (5): djangocms, flaskblogging, telco, tomli_loads, pylint
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x