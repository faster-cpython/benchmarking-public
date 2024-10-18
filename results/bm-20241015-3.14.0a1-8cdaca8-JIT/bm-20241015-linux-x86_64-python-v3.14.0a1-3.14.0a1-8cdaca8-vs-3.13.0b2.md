# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.01x faster
- HPT reliability: 98.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                       |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                     |
| html5lib       | 67.2 ms                                                    | 63.7 ms: 1.06x faster                                      |
| tornado_http   | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                       |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                       |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                       |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 576 ms: 1.06x faster                                       |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 559 ms: 1.05x faster                                       |
| async_tree_io_tg           | 936 ms                                                     | 966 ms: 1.03x slower                                       |
| Geometric mean             | (ref)                                                      | 1.08x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                      |
| float          | 78.9 ms                                                    | 75.4 ms: 1.05x faster                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                      | 1.05x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                       |
| regex_compile  | 137 ms                                                     | 140 ms: 1.03x slower                                       |
| regex_v8       | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.6 ms: 1.11x faster                                      |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                     |
| xml_etree_process    | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                      |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 107 ms                                                     | 99.9 ms: 1.07x faster                                      |
| json_loads           | 28.9 us                                                    | 26.9 us: 1.07x faster                                      |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                       |
| json_dumps           | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                      |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                       |
| pickle_list          | 5.11 us                                                    | 5.20 us: 1.02x slower                                      |
| pickle_dict          | 34.8 us                                                    | 35.8 us: 1.03x slower                                      |
| pickle               | 11.5 us                                                    | 12.0 us: 1.04x slower                                      |
| unpickle_list        | 5.34 us                                                    | 5.59 us: 1.05x slower                                      |
| Geometric mean       | (ref)                                                      | 1.03x faster                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                      |
| python_startup         | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                      |
| Geometric mean         | (ref)                                                      | 1.05x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                      |
| genshi_text     | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                      |
| django_template | 34.8 ms                                                    | 37.2 ms: 1.07x slower                                      |
| genshi_xml      | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                      |
| Geometric mean  | (ref)                                                      | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.4 us: 1.35x faster                                      |
| deepcopy                   | 367 us                                                     | 273 us: 1.35x faster                                       |
| richards                   | 50.9 ms                                                    | 41.0 ms: 1.24x faster                                      |
| scimark_fft                | 392 ms                                                     | 319 ms: 1.23x faster                                       |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                      |
| richards_super             | 57.4 ms                                                    | 48.0 ms: 1.19x faster                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                       |
| crypto_pyaes               | 77.5 ms                                                    | 67.5 ms: 1.15x faster                                      |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.44 sec: 1.13x faster                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.72 ms: 1.12x faster                                      |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.12x faster                                      |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                       |
| xml_etree_generate         | 87.4 ms                                                    | 78.6 ms: 1.11x faster                                      |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                     |
| xml_etree_process          | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                      |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                      |
| async_tree_io              | 939 ms                                                     | 856 ms: 1.10x faster                                       |
| telco                      | 8.41 ms                                                    | 7.68 ms: 1.10x faster                                      |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                       |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                     |
| go                         | 145 ms                                                     | 133 ms: 1.09x faster                                       |
| nbody                      | 88.3 ms                                                    | 81.3 ms: 1.09x faster                                      |
| pyflate                    | 484 ms                                                     | 446 ms: 1.09x faster                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                      |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                       |
| xml_etree_iterparse        | 107 ms                                                     | 99.9 ms: 1.07x faster                                      |
| json_loads                 | 28.9 us                                                    | 26.9 us: 1.07x faster                                      |
| json                       | 5.31 ms                                                    | 4.95 ms: 1.07x faster                                      |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                      |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                      |
| fannkuch                   | 402 ms                                                     | 377 ms: 1.07x faster                                       |
| scimark_lu                 | 122 ms                                                     | 114 ms: 1.06x faster                                       |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 576 ms: 1.06x faster                                       |
| html5lib                   | 67.2 ms                                                    | 63.7 ms: 1.06x faster                                      |
| logging_format             | 6.47 us                                                    | 6.13 us: 1.05x faster                                      |
| async_tree_none_tg         | 336 ms                                                     | 320 ms: 1.05x faster                                       |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 559 ms: 1.05x faster                                       |
| float                      | 78.9 ms                                                    | 75.4 ms: 1.05x faster                                      |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                       |
| pprint_safe_repr           | 758 ms                                                     | 726 ms: 1.05x faster                                       |
| chaos                      | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                       |
| logging_simple             | 5.74 us                                                    | 5.63 us: 1.02x faster                                      |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                       |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                       |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                       |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.01x faster                                       |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.01x faster                                       |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                     |
| dulwich_log                | 67.2 ms                                                    | 66.5 ms: 1.01x faster                                      |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                       |
| tornado_http               | 94.6 ms                                                    | 94.3 ms: 1.00x faster                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.10 ms: 1.00x faster                                      |
| coroutines                 | 23.2 ms                                                    | 23.3 ms: 1.01x slower                                      |
| json_dumps                 | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                      |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                       |
| deltablue                  | 3.25 ms                                                    | 3.29 ms: 1.01x slower                                      |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.01x slower                                       |
| pickle_list                | 5.11 us                                                    | 5.20 us: 1.02x slower                                      |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                      |
| regex_compile              | 137 ms                                                     | 140 ms: 1.03x slower                                       |
| pickle_dict                | 34.8 us                                                    | 35.8 us: 1.03x slower                                      |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                      |
| async_tree_io_tg           | 936 ms                                                     | 966 ms: 1.03x slower                                       |
| raytrace                   | 267 ms                                                     | 276 ms: 1.03x slower                                       |
| pycparser                  | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                     |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.04x slower                                      |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                       |
| unpickle_list              | 5.34 us                                                    | 5.59 us: 1.05x slower                                      |
| regex_v8                   | 25.1 ms                                                    | 26.4 ms: 1.05x slower                                      |
| bench_thread_pool          | 834 us                                                     | 877 us: 1.05x slower                                       |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                       |
| genshi_text                | 23.7 ms                                                    | 25.2 ms: 1.06x slower                                      |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.07x slower                                      |
| django_template            | 34.8 ms                                                    | 37.2 ms: 1.07x slower                                      |
| sympy_str                  | 282 ms                                                     | 303 ms: 1.07x slower                                       |
| async_generators           | 442 ms                                                     | 478 ms: 1.08x slower                                       |
| sqlglot_optimize           | 55.5 ms                                                    | 60.2 ms: 1.08x slower                                      |
| gc_traversal               | 3.98 ms                                                    | 4.40 ms: 1.11x slower                                      |
| python_startup             | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                      |
| hexiom                     | 6.30 ms                                                    | 7.03 ms: 1.12x slower                                      |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                       |
| genshi_xml                 | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                      |
| sympy_integrate            | 20.5 ms                                                    | 23.6 ms: 1.15x slower                                      |
| pylint                     | 317 ms                                                     | 376 ms: 1.18x slower                                       |
| generators                 | 29.6 ms                                                    | 35.4 ms: 1.20x slower                                      |
| create_gc_cycles           | 1.82 ms                                                    | 2.67 ms: 1.47x slower                                      |
| bench_mp_pool              | 23.9 ms                                                    | 84.2 ms: 3.53x slower                                      |
| Geometric mean             | (ref)                                                      | 1.01x faster                                               |

Benchmark hidden because not significant (2): unpickle, regex_effbot
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 98.76% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x