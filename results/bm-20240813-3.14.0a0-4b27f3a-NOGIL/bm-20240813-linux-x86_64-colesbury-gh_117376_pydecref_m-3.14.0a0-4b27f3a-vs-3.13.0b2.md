# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.41x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 395 ms: 1.44x slower                                                     |
| docutils       | 2.83 sec                                                   | 3.33 sec: 1.18x slower                                                   |
| html5lib       | 67.2 ms                                                    | 98.6 ms: 1.47x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 139 ms: 1.47x slower                                                     |
| Geometric mean | (ref)                                                      | 1.38x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                     |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 601 ms: 1.02x slower                                                     |
| async_tree_none_tg         | 336 ms                                                     | 347 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 458 ms: 1.03x slower                                                     |
| async_tree_none            | 378 ms                                                     | 406 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 659 ms: 1.08x slower                                                     |
| async_tree_memoization     | 463 ms                                                     | 510 ms: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.02x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 184 ms: 1.04x faster                                                     |
| float          | 78.9 ms                                                    | 139 ms: 1.77x slower                                                     |
| nbody          | 88.3 ms                                                    | 223 ms: 2.52x slower                                                     |
| Geometric mean | (ref)                                                      | 1.62x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                                    |
| regex_dna      | 221 ms                                                     | 220 ms: 1.00x faster                                                     |
| regex_v8       | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                    |
| regex_compile  | 137 ms                                                     | 217 ms: 1.59x slower                                                     |
| Geometric mean | (ref)                                                      | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 114 ms: 1.06x slower                                                     |
| json_loads           | 28.9 us                                                    | 31.6 us: 1.09x slower                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 110 ms: 1.26x slower                                                     |
| json_dumps           | 10.7 ms                                                    | 13.6 ms: 1.27x slower                                                    |
| xml_etree_process    | 61.2 ms                                                    | 88.3 ms: 1.44x slower                                                    |
| tomli_loads          | 2.12 sec                                                   | 3.22 sec: 1.52x slower                                                   |
| unpickle_pure_python | 218 us                                                     | 408 us: 1.87x slower                                                     |
| pickle_pure_python   | 305 us                                                     | 575 us: 1.88x slower                                                     |
| Geometric mean       | (ref)                                                      | 1.34x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.7 ms: 1.27x slower                                                    |
| python_startup_no_site | 7.11 ms                                                    | 9.30 ms: 1.31x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.29x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 82.4 ms: 1.60x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 39.9 ms: 1.69x slower                                                    |
| django_template | 34.8 ms                                                    | 59.8 ms: 1.72x slower                                                    |
| mako            | 11.2 ms                                                    | 21.1 ms: 1.88x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.72x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 1.82 ms                                                    | 1.38 ms: 1.32x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.03 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 830 ms: 1.13x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.06x faster                                                     |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                     |
| pidigits                   | 191 ms                                                     | 184 ms: 1.04x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.54 ms: 1.04x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                     |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.00x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 601 ms: 1.02x slower                                                     |
| async_tree_none_tg         | 336 ms                                                     | 347 ms: 1.03x slower                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 458 ms: 1.03x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 26.0 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 114 ms: 1.06x slower                                                     |
| async_tree_none            | 378 ms                                                     | 406 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 659 ms: 1.08x slower                                                     |
| pathlib                    | 17.3 ms                                                    | 18.9 ms: 1.09x slower                                                    |
| json_loads                 | 28.9 us                                                    | 31.6 us: 1.09x slower                                                    |
| async_tree_memoization     | 463 ms                                                     | 510 ms: 1.10x slower                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.05 sec: 1.11x slower                                                   |
| asyncio_tcp                | 508 ms                                                     | 568 ms: 1.12x slower                                                     |
| json                       | 5.31 ms                                                    | 5.93 ms: 1.12x slower                                                    |
| mdp                        | 2.79 sec                                                   | 3.19 sec: 1.14x slower                                                   |
| deepcopy                   | 367 us                                                     | 421 us: 1.15x slower                                                     |
| docutils                   | 2.83 sec                                                   | 3.33 sec: 1.18x slower                                                   |
| telco                      | 8.41 ms                                                    | 10.2 ms: 1.21x slower                                                    |
| generators                 | 29.6 ms                                                    | 36.4 ms: 1.23x slower                                                    |
| scimark_fft                | 392 ms                                                     | 483 ms: 1.23x slower                                                     |
| pylint                     | 317 ms                                                     | 392 ms: 1.24x slower                                                     |
| coverage                   | 93.1 ms                                                    | 116 ms: 1.25x slower                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 110 ms: 1.26x slower                                                     |
| async_generators           | 442 ms                                                     | 557 ms: 1.26x slower                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.69 ms: 1.27x slower                                                    |
| json_dumps                 | 10.7 ms                                                    | 13.6 ms: 1.27x slower                                                    |
| python_startup             | 10.8 ms                                                    | 13.7 ms: 1.27x slower                                                    |
| meteor_contest             | 110 ms                                                     | 141 ms: 1.28x slower                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 6.57 sec: 1.31x slower                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 9.30 ms: 1.31x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 4.39 us: 1.31x slower                                                    |
| deepcopy_memo              | 39.7 us                                                    | 53.2 us: 1.34x slower                                                    |
| coroutines                 | 23.2 ms                                                    | 31.6 ms: 1.36x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.62 sec: 1.39x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 28.7 ms: 1.40x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 117 ms: 1.43x slower                                                     |
| 2to3                       | 274 ms                                                     | 395 ms: 1.44x slower                                                     |
| xml_etree_process          | 61.2 ms                                                    | 88.3 ms: 1.44x slower                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 113 ms: 1.46x slower                                                     |
| html5lib                   | 67.2 ms                                                    | 98.6 ms: 1.47x slower                                                    |
| tornado_http               | 94.6 ms                                                    | 139 ms: 1.47x slower                                                     |
| sympy_str                  | 282 ms                                                     | 422 ms: 1.49x slower                                                     |
| thrift                     | 823 us                                                     | 1.23 ms: 1.50x slower                                                    |
| fannkuch                   | 402 ms                                                     | 605 ms: 1.51x slower                                                     |
| tomli_loads                | 2.12 sec                                                   | 3.22 sec: 1.52x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 251 us: 1.53x slower                                                     |
| sqlglot_normalize          | 110 ms                                                     | 171 ms: 1.55x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 86.6 ms: 1.56x slower                                                    |
| richards                   | 50.9 ms                                                    | 80.1 ms: 1.57x slower                                                    |
| spectral_norm              | 116 ms                                                     | 183 ms: 1.57x slower                                                     |
| sympy_expand               | 473 ms                                                     | 746 ms: 1.58x slower                                                     |
| pyflate                    | 484 ms                                                     | 765 ms: 1.58x slower                                                     |
| regex_compile              | 137 ms                                                     | 217 ms: 1.59x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 82.4 ms: 1.60x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 256 ms: 1.64x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 39.9 ms: 1.69x slower                                                    |
| pprint_safe_repr           | 758 ms                                                     | 1.28 sec: 1.69x slower                                                   |
| richards_super             | 57.4 ms                                                    | 97.2 ms: 1.69x slower                                                    |
| pprint_pformat             | 1.56 sec                                                   | 2.66 sec: 1.71x slower                                                   |
| django_template            | 34.8 ms                                                    | 59.8 ms: 1.72x slower                                                    |
| comprehensions             | 16.6 us                                                    | 28.8 us: 1.73x slower                                                    |
| float                      | 78.9 ms                                                    | 139 ms: 1.77x slower                                                     |
| logging_format             | 6.47 us                                                    | 11.7 us: 1.80x slower                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 125 ms: 1.81x slower                                                     |
| logging_simple             | 5.74 us                                                    | 10.4 us: 1.82x slower                                                    |
| unpickle_pure_python       | 218 us                                                     | 408 us: 1.87x slower                                                     |
| mako                       | 11.2 ms                                                    | 21.1 ms: 1.88x slower                                                    |
| pickle_pure_python         | 305 us                                                     | 575 us: 1.88x slower                                                     |
| logging_silent             | 105 ns                                                     | 197 ns: 1.88x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 3.10 ms: 1.90x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 12.0 ms: 1.91x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 238 ms: 1.96x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 2.63 ms: 1.99x slower                                                    |
| chaos                      | 61.3 ms                                                    | 125 ms: 2.04x slower                                                     |
| scimark_sor                | 127 ms                                                     | 268 ms: 2.10x slower                                                     |
| go                         | 145 ms                                                     | 309 ms: 2.14x slower                                                     |
| raytrace                   | 267 ms                                                     | 603 ms: 2.26x slower                                                     |
| nbody                      | 88.3 ms                                                    | 223 ms: 2.52x slower                                                     |
| deltablue                  | 3.25 ms                                                    | 8.38 ms: 2.58x slower                                                    |
| bench_thread_pool          | 834 us                                                     | 3.12 ms: 3.74x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.41x slower                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.16x