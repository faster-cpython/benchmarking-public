# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.00x slower
- HPT reliability: 98.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.02x faster                                       |
| chameleon      | 7.22 ms                                                    | 6.83 ms: 1.06x faster                                      |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                     |
| tornado_http   | 94.6 ms                                                    | 98.6 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 449 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 729 ms: 1.19x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 581 ms: 1.25x slower                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 745 ms: 1.27x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.24 sec: 1.32x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 595 ms: 1.34x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 463 ms: 1.38x slower                                       |
| Geometric mean             | (ref)                                                      | 1.28x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| float          | 78.9 ms                                                    | 82.6 ms: 1.05x slower                                      |
| nbody          | 88.3 ms                                                    | 93.6 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                      | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                      |
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                       |
| regex_dna      | 221 ms                                                     | 216 ms: 1.03x faster                                       |
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                      | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 5.34 us                                                    | 5.05 us: 1.06x faster                                      |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                      |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                      |
| pickle_list          | 5.11 us                                                    | 5.01 us: 1.02x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.01x faster                                       |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                       |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                       |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.01x faster                                       |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                     |
| pickle_dict          | 34.8 us                                                    | 35.7 us: 1.03x slower                                      |
| Geometric mean       | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (3): unpickle, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                      |
| python_startup_no_site | 7.11 ms                                                    | 8.99 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                      | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                      |
| django_template | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                      |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                      | 1.01x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 165 us                                                     | 112 us: 1.47x faster                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.52 ms: 1.20x faster                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.68 ms: 1.13x faster                                      |
| richards                   | 50.9 ms                                                    | 45.9 ms: 1.11x faster                                      |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.10x faster                                      |
| deepcopy_reduce            | 3.35 us                                                    | 3.04 us: 1.10x faster                                      |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                     |
| scimark_fft                | 392 ms                                                     | 362 ms: 1.08x faster                                       |
| spectral_norm              | 116 ms                                                     | 108 ms: 1.08x faster                                       |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                       |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                     |
| crypto_pyaes               | 77.5 ms                                                    | 73.0 ms: 1.06x faster                                      |
| deepcopy                   | 367 us                                                     | 346 us: 1.06x faster                                       |
| unpickle_list              | 5.34 us                                                    | 5.05 us: 1.06x faster                                      |
| chameleon                  | 7.22 ms                                                    | 6.83 ms: 1.06x faster                                      |
| coroutines                 | 23.2 ms                                                    | 22.0 ms: 1.05x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                      |
| logging_silent             | 105 ns                                                     | 99.5 ns: 1.05x faster                                      |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                       |
| thrift                     | 823 us                                                     | 790 us: 1.04x faster                                       |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                      |
| deepcopy_memo              | 39.7 us                                                    | 38.1 us: 1.04x faster                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                      |
| regex_effbot               | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                      |
| scimark_sor                | 127 ms                                                     | 123 ms: 1.04x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.89 us: 1.04x faster                                      |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                       |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                      |
| pyflate                    | 484 ms                                                     | 469 ms: 1.03x faster                                       |
| json                       | 5.31 ms                                                    | 5.15 ms: 1.03x faster                                      |
| genshi_text                | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                      |
| django_template            | 34.8 ms                                                    | 33.8 ms: 1.03x faster                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 53.9 ms: 1.03x faster                                      |
| regex_compile              | 137 ms                                                     | 133 ms: 1.03x faster                                       |
| sympy_str                  | 282 ms                                                     | 275 ms: 1.03x faster                                       |
| hexiom                     | 6.30 ms                                                    | 6.13 ms: 1.03x faster                                      |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.03x faster                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                      |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.02x faster                                      |
| xml_etree_process          | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                      |
| flaskblogging              | 9.01 ms                                                    | 8.82 ms: 1.02x faster                                      |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.9 ms: 1.02x faster                                      |
| pickle_list                | 5.11 us                                                    | 5.01 us: 1.02x faster                                      |
| sympy_sum                  | 156 ms                                                     | 153 ms: 1.02x faster                                       |
| 2to3                       | 274 ms                                                     | 270 ms: 1.02x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 159 ms: 1.01x faster                                       |
| sympy_expand               | 473 ms                                                     | 466 ms: 1.01x faster                                       |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                       |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                      |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                       |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                       |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                       |
| nqueens                    | 81.4 ms                                                    | 80.7 ms: 1.01x faster                                      |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                       |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                      |
| chaos                      | 61.3 ms                                                    | 60.9 ms: 1.01x faster                                      |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.01x faster                                       |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 563 ms: 1.01x faster                                       |
| fannkuch                   | 402 ms                                                     | 400 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                     |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                      |
| genshi_xml                 | 51.6 ms                                                    | 52.0 ms: 1.01x slower                                      |
| gunicorn                   | 1.28 ms                                                    | 1.29 ms: 1.01x slower                                      |
| aiohttp                    | 1.18 ms                                                    | 1.19 ms: 1.01x slower                                      |
| logging_format             | 6.47 us                                                    | 6.53 us: 1.01x slower                                      |
| bench_thread_pool          | 834 us                                                     | 842 us: 1.01x slower                                       |
| async_generators           | 442 ms                                                     | 449 ms: 1.02x slower                                       |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                      |
| tomli_loads                | 2.12 sec                                                   | 2.16 sec: 1.02x slower                                     |
| logging_simple             | 5.74 us                                                    | 5.85 us: 1.02x slower                                      |
| djangocms                  | 31.5 us                                                    | 32.1 us: 1.02x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                     |
| telco                      | 8.41 ms                                                    | 8.60 ms: 1.02x slower                                      |
| coverage                   | 93.1 ms                                                    | 95.6 ms: 1.03x slower                                      |
| pickle_dict                | 34.8 us                                                    | 35.7 us: 1.03x slower                                      |
| tornado_http               | 94.6 ms                                                    | 98.6 ms: 1.04x slower                                      |
| float                      | 78.9 ms                                                    | 82.6 ms: 1.05x slower                                      |
| nbody                      | 88.3 ms                                                    | 93.6 ms: 1.06x slower                                      |
| pathlib                    | 17.3 ms                                                    | 18.5 ms: 1.07x slower                                      |
| mypy2                      | 742 ms                                                     | 871 ms: 1.17x slower                                       |
| async_tree_none            | 378 ms                                                     | 449 ms: 1.19x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 729 ms: 1.19x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 581 ms: 1.25x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 8.99 ms: 1.26x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 745 ms: 1.27x slower                                       |
| async_tree_io              | 939 ms                                                     | 1.22 sec: 1.30x slower                                     |
| async_tree_io_tg           | 936 ms                                                     | 1.24 sec: 1.32x slower                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 595 ms: 1.34x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 463 ms: 1.38x slower                                       |
| Geometric mean             | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (11): pylint, generators, unpickle, pprint_safe_repr, xml_etree_generate, pprint_pformat, bench_mp_pool, dask, html5lib, dulwich_log, json_dumps
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 98.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x