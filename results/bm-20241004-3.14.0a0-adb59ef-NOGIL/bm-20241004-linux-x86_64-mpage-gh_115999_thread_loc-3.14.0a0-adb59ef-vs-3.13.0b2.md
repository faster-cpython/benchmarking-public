# Results vs. 3.13.0b2

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 393 ms: 1.43x slower                                                 |
| docutils       | 2.83 sec                                                   | 3.24 sec: 1.15x slower                                               |
| html5lib       | 67.2 ms                                                    | 93.9 ms: 1.40x slower                                                |
| tornado_http   | 94.6 ms                                                    | 138 ms: 1.46x slower                                                 |
| Geometric mean | (ref)                                                      | 1.35x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 836 ms: 1.12x faster                                                 |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 603 ms: 1.03x slower                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 457 ms: 1.03x slower                                                 |
| async_tree_none_tg         | 336 ms                                                     | 356 ms: 1.06x slower                                                 |
| async_tree_none            | 378 ms                                                     | 402 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 656 ms: 1.07x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 505 ms: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 183 ms: 1.04x faster                                                 |
| float          | 78.9 ms                                                    | 137 ms: 1.74x slower                                                 |
| nbody          | 88.3 ms                                                    | 189 ms: 2.14x slower                                                 |
| Geometric mean | (ref)                                                      | 1.53x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                                |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                |
| regex_compile  | 137 ms                                                     | 213 ms: 1.56x slower                                                 |
| Geometric mean | (ref)                                                      | 1.11x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                 |
| pickle_list          | 5.11 us                                                    | 4.75 us: 1.07x faster                                                |
| pickle               | 11.5 us                                                    | 10.7 us: 1.07x faster                                                |
| pickle_dict          | 34.8 us                                                    | 33.0 us: 1.05x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.49 us: 1.03x slower                                                |
| xml_etree_iterparse  | 107 ms                                                     | 112 ms: 1.04x slower                                                 |
| json_loads           | 28.9 us                                                    | 30.3 us: 1.05x slower                                                |
| unpickle             | 15.1 us                                                    | 15.9 us: 1.05x slower                                                |
| json_dumps           | 10.7 ms                                                    | 12.8 ms: 1.20x slower                                                |
| xml_etree_generate   | 87.4 ms                                                    | 108 ms: 1.24x slower                                                 |
| xml_etree_process    | 61.2 ms                                                    | 86.8 ms: 1.42x slower                                                |
| tomli_loads          | 2.12 sec                                                   | 3.17 sec: 1.49x slower                                               |
| unpickle_pure_python | 218 us                                                     | 390 us: 1.79x slower                                                 |
| pickle_pure_python   | 305 us                                                     | 564 us: 1.85x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.17x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 14.3 ms: 1.33x slower                                                |
| python_startup_no_site | 7.11 ms                                                    | 9.52 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                      | 1.33x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 83.2 ms: 1.61x slower                                                |
| genshi_text     | 23.7 ms                                                    | 39.9 ms: 1.68x slower                                                |
| django_template | 34.8 ms                                                    | 59.7 ms: 1.71x slower                                                |
| mako            | 11.2 ms                                                    | 20.7 ms: 1.84x slower                                                |
| Geometric mean  | (ref)                                                      | 1.71x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal               | 3.98 ms                                                    | 2.90 ms: 1.37x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.39 ms: 1.30x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 836 ms: 1.12x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                 |
| pickle_list                | 5.11 us                                                    | 4.75 us: 1.07x faster                                                |
| pickle                     | 11.5 us                                                    | 10.7 us: 1.07x faster                                                |
| pickle_dict                | 34.8 us                                                    | 33.0 us: 1.05x faster                                                |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                                 |
| pidigits                   | 191 ms                                                     | 183 ms: 1.04x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                                |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                 |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 603 ms: 1.03x slower                                                 |
| unpickle_list              | 5.34 us                                                    | 5.49 us: 1.03x slower                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 457 ms: 1.03x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 112 ms: 1.04x slower                                                 |
| sqlite_synth               | 2.99 us                                                    | 3.14 us: 1.05x slower                                                |
| json_loads                 | 28.9 us                                                    | 30.3 us: 1.05x slower                                                |
| unpickle                   | 15.1 us                                                    | 15.9 us: 1.05x slower                                                |
| json                       | 5.31 ms                                                    | 5.60 ms: 1.06x slower                                                |
| async_tree_none_tg         | 336 ms                                                     | 356 ms: 1.06x slower                                                 |
| async_tree_none            | 378 ms                                                     | 402 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 656 ms: 1.07x slower                                                 |
| scimark_fft                | 392 ms                                                     | 422 ms: 1.08x slower                                                 |
| async_tree_memoization     | 463 ms                                                     | 505 ms: 1.09x slower                                                 |
| asyncio_tcp                | 508 ms                                                     | 558 ms: 1.10x slower                                                 |
| pathlib                    | 17.3 ms                                                    | 19.1 ms: 1.10x slower                                                |
| deepcopy                   | 367 us                                                     | 408 us: 1.11x slower                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.88 ms: 1.12x slower                                                |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.07 sec: 1.12x slower                                               |
| docutils                   | 2.83 sec                                                   | 3.24 sec: 1.15x slower                                               |
| coverage                   | 93.1 ms                                                    | 108 ms: 1.16x slower                                                 |
| telco                      | 8.41 ms                                                    | 9.92 ms: 1.18x slower                                                |
| mdp                        | 2.79 sec                                                   | 3.32 sec: 1.19x slower                                               |
| json_dumps                 | 10.7 ms                                                    | 12.8 ms: 1.20x slower                                                |
| async_generators           | 442 ms                                                     | 531 ms: 1.20x slower                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 108 ms: 1.24x slower                                                 |
| pylint                     | 317 ms                                                     | 394 ms: 1.24x slower                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 6.34 sec: 1.26x slower                                               |
| deepcopy_reduce            | 3.35 us                                                    | 4.23 us: 1.26x slower                                                |
| generators                 | 29.6 ms                                                    | 38.0 ms: 1.28x slower                                                |
| meteor_contest             | 110 ms                                                     | 141 ms: 1.28x slower                                                 |
| deepcopy_memo              | 39.7 us                                                    | 51.4 us: 1.29x slower                                                |
| coroutines                 | 23.2 ms                                                    | 30.1 ms: 1.30x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 87.6 ms: 1.30x slower                                                |
| python_startup             | 10.8 ms                                                    | 14.3 ms: 1.33x slower                                                |
| python_startup_no_site     | 7.11 ms                                                    | 9.52 ms: 1.34x slower                                                |
| pycparser                  | 1.16 sec                                                   | 1.60 sec: 1.38x slower                                               |
| html5lib                   | 67.2 ms                                                    | 93.9 ms: 1.40x slower                                                |
| spectral_norm              | 116 ms                                                     | 163 ms: 1.40x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 114 ms: 1.41x slower                                                 |
| xml_etree_process          | 61.2 ms                                                    | 86.8 ms: 1.42x slower                                                |
| crypto_pyaes               | 77.5 ms                                                    | 110 ms: 1.42x slower                                                 |
| 2to3                       | 274 ms                                                     | 393 ms: 1.43x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 29.4 ms: 1.44x slower                                                |
| fannkuch                   | 402 ms                                                     | 585 ms: 1.46x slower                                                 |
| tornado_http               | 94.6 ms                                                    | 138 ms: 1.46x slower                                                 |
| thrift                     | 823 us                                                     | 1.22 ms: 1.49x slower                                                |
| typing_runtime_protocols   | 165 us                                                     | 246 us: 1.49x slower                                                 |
| tomli_loads                | 2.12 sec                                                   | 3.17 sec: 1.49x slower                                               |
| sympy_str                  | 282 ms                                                     | 429 ms: 1.52x slower                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 84.5 ms: 1.52x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 168 ms: 1.53x slower                                                 |
| richards                   | 50.9 ms                                                    | 78.0 ms: 1.53x slower                                                |
| pyflate                    | 484 ms                                                     | 751 ms: 1.55x slower                                                 |
| regex_compile              | 137 ms                                                     | 213 ms: 1.56x slower                                                 |
| sympy_expand               | 473 ms                                                     | 758 ms: 1.60x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 83.2 ms: 1.61x slower                                                |
| pprint_safe_repr           | 758 ms                                                     | 1.25 sec: 1.65x slower                                               |
| pprint_pformat             | 1.56 sec                                                   | 2.58 sec: 1.66x slower                                               |
| richards_super             | 57.4 ms                                                    | 95.6 ms: 1.67x slower                                                |
| genshi_text                | 23.7 ms                                                    | 39.9 ms: 1.68x slower                                                |
| scimark_monte_carlo        | 69.2 ms                                                    | 117 ms: 1.70x slower                                                 |
| sympy_sum                  | 156 ms                                                     | 265 ms: 1.70x slower                                                 |
| comprehensions             | 16.6 us                                                    | 28.4 us: 1.71x slower                                                |
| django_template            | 34.8 ms                                                    | 59.7 ms: 1.71x slower                                                |
| logging_format             | 6.47 us                                                    | 11.2 us: 1.74x slower                                                |
| float                      | 78.9 ms                                                    | 137 ms: 1.74x slower                                                 |
| logging_simple             | 5.74 us                                                    | 10.2 us: 1.78x slower                                                |
| unpickle_pure_python       | 218 us                                                     | 390 us: 1.79x slower                                                 |
| scimark_lu                 | 122 ms                                                     | 221 ms: 1.82x slower                                                 |
| chaos                      | 61.3 ms                                                    | 112 ms: 1.82x slower                                                 |
| mako                       | 11.2 ms                                                    | 20.7 ms: 1.84x slower                                                |
| go                         | 145 ms                                                     | 267 ms: 1.85x slower                                                 |
| pickle_pure_python         | 305 us                                                     | 564 us: 1.85x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 11.7 ms: 1.87x slower                                                |
| logging_silent             | 105 ns                                                     | 195 ns: 1.87x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 3.07 ms: 1.88x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 2.60 ms: 1.97x slower                                                |
| scimark_sor                | 127 ms                                                     | 251 ms: 1.97x slower                                                 |
| raytrace                   | 267 ms                                                     | 564 ms: 2.12x slower                                                 |
| nbody                      | 88.3 ms                                                    | 189 ms: 2.14x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 8.21 ms: 2.52x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 66.3 ms: 2.77x slower                                                |
| bench_thread_pool          | 834 us                                                     | 3.44 ms: 4.13x slower                                                |
| Geometric mean             | (ref)                                                      | 1.36x slower                                                         |
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-adb59ef-NOGIL/bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.27x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.17x