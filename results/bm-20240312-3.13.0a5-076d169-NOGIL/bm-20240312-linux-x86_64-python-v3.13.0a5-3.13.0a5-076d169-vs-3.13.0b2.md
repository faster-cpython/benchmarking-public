# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 377 ms: 1.38x slower                                       |
| chameleon      | 7.22 ms                                                    | 12.3 ms: 1.70x slower                                      |
| docutils       | 2.83 sec                                                   | 3.28 sec: 1.16x slower                                     |
| html5lib       | 67.2 ms                                                    | 91.5 ms: 1.36x slower                                      |
| tornado_http   | 94.6 ms                                                    | 137 ms: 1.45x slower                                       |
| Geometric mean | (ref)                                                      | 1.40x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 839 ms: 1.12x faster                                       |
| async_tree_io              | 939 ms                                                     | 877 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 623 ms: 1.06x slower                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 472 ms: 1.06x slower                                       |
| async_tree_none            | 378 ms                                                     | 412 ms: 1.09x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 668 ms: 1.09x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 369 ms: 1.10x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 518 ms: 1.12x slower                                       |
| Geometric mean             | (ref)                                                      | 1.04x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 192 ms: 1.00x slower                                       |
| float          | 78.9 ms                                                    | 127 ms: 1.60x slower                                       |
| nbody          | 88.3 ms                                                    | 215 ms: 2.43x slower                                       |
| Geometric mean | (ref)                                                      | 1.58x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                      |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                       |
| regex_v8       | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                      |
| regex_compile  | 137 ms                                                     | 204 ms: 1.49x slower                                       |
| Geometric mean | (ref)                                                      | 1.13x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                       |
| pickle_list          | 5.11 us                                                    | 4.97 us: 1.03x faster                                      |
| pickle               | 11.5 us                                                    | 12.1 us: 1.05x slower                                      |
| unpickle_list        | 5.34 us                                                    | 5.75 us: 1.08x slower                                      |
| xml_etree_iterparse  | 107 ms                                                     | 117 ms: 1.09x slower                                       |
| pickle_dict          | 34.8 us                                                    | 41.4 us: 1.19x slower                                      |
| unpickle             | 15.1 us                                                    | 18.1 us: 1.20x slower                                      |
| json_loads           | 28.9 us                                                    | 34.8 us: 1.20x slower                                      |
| xml_etree_generate   | 87.4 ms                                                    | 108 ms: 1.23x slower                                       |
| json_dumps           | 10.7 ms                                                    | 13.7 ms: 1.28x slower                                      |
| xml_etree_process    | 61.2 ms                                                    | 86.4 ms: 1.41x slower                                      |
| tomli_loads          | 2.12 sec                                                   | 3.11 sec: 1.47x slower                                     |
| unpickle_pure_python | 218 us                                                     | 367 us: 1.68x slower                                       |
| pickle_pure_python   | 305 us                                                     | 528 us: 1.73x slower                                       |
| Geometric mean       | (ref)                                                      | 1.23x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.6 ms: 1.27x slower                                      |
| python_startup_no_site | 7.11 ms                                                    | 11.6 ms: 1.63x slower                                      |
| Geometric mean         | (ref)                                                      | 1.44x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 78.4 ms: 1.52x slower                                      |
| genshi_text     | 23.7 ms                                                    | 38.9 ms: 1.64x slower                                      |
| django_template | 34.8 ms                                                    | 57.7 ms: 1.66x slower                                      |
| mako            | 11.2 ms                                                    | 21.0 ms: 1.87x slower                                      |
| Geometric mean  | (ref)                                                      | 1.67x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.08 ms: 1.68x faster                                      |
| gc_traversal               | 3.98 ms                                                    | 2.57 ms: 1.55x faster                                      |
| async_tree_io_tg           | 936 ms                                                     | 839 ms: 1.12x faster                                       |
| async_tree_io              | 939 ms                                                     | 877 ms: 1.07x faster                                       |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                       |
| regex_effbot               | 3.67 ms                                                    | 3.56 ms: 1.03x faster                                      |
| pickle_list                | 5.11 us                                                    | 4.97 us: 1.03x faster                                      |
| pidigits                   | 191 ms                                                     | 192 ms: 1.00x slower                                       |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                       |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                       |
| pickle                     | 11.5 us                                                    | 12.1 us: 1.05x slower                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 623 ms: 1.06x slower                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 472 ms: 1.06x slower                                       |
| regex_v8                   | 25.1 ms                                                    | 26.9 ms: 1.07x slower                                      |
| unpickle_list              | 5.34 us                                                    | 5.75 us: 1.08x slower                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.99 sec: 1.08x slower                                     |
| async_tree_none            | 378 ms                                                     | 412 ms: 1.09x slower                                       |
| xml_etree_iterparse        | 107 ms                                                     | 117 ms: 1.09x slower                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 668 ms: 1.09x slower                                       |
| async_tree_none_tg         | 336 ms                                                     | 369 ms: 1.10x slower                                       |
| async_tree_memoization     | 463 ms                                                     | 518 ms: 1.12x slower                                       |
| asyncio_tcp                | 508 ms                                                     | 584 ms: 1.15x slower                                       |
| async_generators           | 442 ms                                                     | 511 ms: 1.16x slower                                       |
| docutils                   | 2.83 sec                                                   | 3.28 sec: 1.16x slower                                     |
| json                       | 5.31 ms                                                    | 6.24 ms: 1.18x slower                                      |
| mdp                        | 2.79 sec                                                   | 3.30 sec: 1.18x slower                                     |
| pickle_dict                | 34.8 us                                                    | 41.4 us: 1.19x slower                                      |
| unpickle                   | 15.1 us                                                    | 18.1 us: 1.20x slower                                      |
| json_loads                 | 28.9 us                                                    | 34.8 us: 1.20x slower                                      |
| generators                 | 29.6 ms                                                    | 36.2 ms: 1.22x slower                                      |
| scimark_fft                | 392 ms                                                     | 481 ms: 1.23x slower                                       |
| pylint                     | 317 ms                                                     | 390 ms: 1.23x slower                                       |
| xml_etree_generate         | 87.4 ms                                                    | 108 ms: 1.23x slower                                       |
| meteor_contest             | 110 ms                                                     | 136 ms: 1.23x slower                                       |
| coroutines                 | 23.2 ms                                                    | 29.3 ms: 1.26x slower                                      |
| python_startup             | 10.8 ms                                                    | 13.6 ms: 1.27x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 13.7 ms: 1.28x slower                                      |
| sqlite_synth               | 2.99 us                                                    | 3.84 us: 1.28x slower                                      |
| dulwich_log                | 67.2 ms                                                    | 89.2 ms: 1.33x slower                                      |
| richards                   | 50.9 ms                                                    | 68.0 ms: 1.34x slower                                      |
| gunicorn                   | 1.28 ms                                                    | 1.71 ms: 1.34x slower                                      |
| aiohttp                    | 1.18 ms                                                    | 1.59 ms: 1.35x slower                                      |
| pycparser                  | 1.16 sec                                                   | 1.57 sec: 1.36x slower                                     |
| html5lib                   | 67.2 ms                                                    | 91.5 ms: 1.36x slower                                      |
| nqueens                    | 81.4 ms                                                    | 111 ms: 1.37x slower                                       |
| 2to3                       | 274 ms                                                     | 377 ms: 1.38x slower                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 7.26 ms: 1.38x slower                                      |
| sympy_integrate            | 20.5 ms                                                    | 28.4 ms: 1.39x slower                                      |
| telco                      | 8.41 ms                                                    | 11.7 ms: 1.39x slower                                      |
| fannkuch                   | 402 ms                                                     | 559 ms: 1.39x slower                                       |
| crypto_pyaes               | 77.5 ms                                                    | 108 ms: 1.40x slower                                       |
| xml_etree_process          | 61.2 ms                                                    | 86.4 ms: 1.41x slower                                      |
| deepcopy_reduce            | 3.35 us                                                    | 4.74 us: 1.42x slower                                      |
| richards_super             | 57.4 ms                                                    | 82.3 ms: 1.43x slower                                      |
| deepcopy                   | 367 us                                                     | 527 us: 1.43x slower                                       |
| mypy2                      | 742 ms                                                     | 1.07 sec: 1.45x slower                                     |
| tornado_http               | 94.6 ms                                                    | 137 ms: 1.45x slower                                       |
| tomli_loads                | 2.12 sec                                                   | 3.11 sec: 1.47x slower                                     |
| sympy_str                  | 282 ms                                                     | 421 ms: 1.49x slower                                       |
| regex_compile              | 137 ms                                                     | 204 ms: 1.49x slower                                       |
| pathlib                    | 17.3 ms                                                    | 25.9 ms: 1.49x slower                                      |
| pyflate                    | 484 ms                                                     | 728 ms: 1.50x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 78.4 ms: 1.52x slower                                      |
| deepcopy_memo              | 39.7 us                                                    | 60.8 us: 1.53x slower                                      |
| comprehensions             | 16.6 us                                                    | 25.7 us: 1.54x slower                                      |
| spectral_norm              | 116 ms                                                     | 181 ms: 1.56x slower                                       |
| sympy_expand               | 473 ms                                                     | 740 ms: 1.57x slower                                       |
| pprint_safe_repr           | 758 ms                                                     | 1.20 sec: 1.58x slower                                     |
| flaskblogging              | 9.01 ms                                                    | 14.3 ms: 1.59x slower                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 88.8 ms: 1.60x slower                                      |
| pprint_pformat             | 1.56 sec                                                   | 2.49 sec: 1.60x slower                                     |
| float                      | 78.9 ms                                                    | 127 ms: 1.60x slower                                       |
| sqlglot_normalize          | 110 ms                                                     | 177 ms: 1.61x slower                                       |
| sympy_sum                  | 156 ms                                                     | 254 ms: 1.63x slower                                       |
| python_startup_no_site     | 7.11 ms                                                    | 11.6 ms: 1.63x slower                                      |
| genshi_text                | 23.7 ms                                                    | 38.9 ms: 1.64x slower                                      |
| django_template            | 34.8 ms                                                    | 57.7 ms: 1.66x slower                                      |
| unpickle_pure_python       | 218 us                                                     | 367 us: 1.68x slower                                       |
| logging_silent             | 105 ns                                                     | 176 ns: 1.68x slower                                       |
| chameleon                  | 7.22 ms                                                    | 12.3 ms: 1.70x slower                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 119 ms: 1.72x slower                                       |
| pickle_pure_python         | 305 us                                                     | 528 us: 1.73x slower                                       |
| logging_format             | 6.47 us                                                    | 11.2 us: 1.73x slower                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 2.84 ms: 1.74x slower                                      |
| hexiom                     | 6.30 ms                                                    | 11.0 ms: 1.75x slower                                      |
| logging_simple             | 5.74 us                                                    | 10.2 us: 1.77x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 2.37 ms: 1.80x slower                                      |
| mako                       | 11.2 ms                                                    | 21.0 ms: 1.87x slower                                      |
| chaos                      | 61.3 ms                                                    | 115 ms: 1.88x slower                                       |
| scimark_sor                | 127 ms                                                     | 241 ms: 1.89x slower                                       |
| go                         | 145 ms                                                     | 273 ms: 1.89x slower                                       |
| raytrace                   | 267 ms                                                     | 518 ms: 1.94x slower                                       |
| scimark_lu                 | 122 ms                                                     | 250 ms: 2.06x slower                                       |
| deltablue                  | 3.25 ms                                                    | 7.43 ms: 2.29x slower                                      |
| nbody                      | 88.3 ms                                                    | 215 ms: 2.43x slower                                       |
| bench_thread_pool          | 834 us                                                     | 3.01 ms: 3.61x slower                                      |
| coverage                   | 93.1 ms                                                    | 891 ms: 9.57x slower                                       |
| thrift                     | 823 us                                                     | 12.4 ms: 15.05x slower                                     |
| Geometric mean             | (ref)                                                      | 1.43x slower                                               |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (3) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask, djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.30x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: 1.09x