# Results vs. 3.13.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 395 ms: 1.49x slower                                                     |
| docutils       | 2.58 sec                                               | 3.33 sec: 1.29x slower                                                   |
| html5lib       | 64.5 ms                                                | 98.6 ms: 1.53x slower                                                    |
| tornado_http   | 91.5 ms                                                | 139 ms: 1.52x slower                                                     |
| Geometric mean | (ref)                                                  | 1.45x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 458 ms: 1.01x faster                                                     |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                     |
| async_tree_none_tg         | 320 ms                                                 | 347 ms: 1.08x slower                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 601 ms: 1.11x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.05 sec: 1.14x slower                                                   |
| async_tree_none            | 354 ms                                                 | 406 ms: 1.15x slower                                                     |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 659 ms: 1.15x slower                                                     |
| async_tree_memoization     | 442 ms                                                 | 510 ms: 1.15x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 568 ms: 1.16x slower                                                     |
| async_generators           | 433 ms                                                 | 557 ms: 1.29x slower                                                     |
| coroutines                 | 22.5 ms                                                | 31.6 ms: 1.40x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.12x slower                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 184 ms: 1.01x faster                                                     |
| float          | 78.5 ms                                                | 139 ms: 1.77x slower                                                     |
| nbody          | 85.7 ms                                                | 223 ms: 2.60x slower                                                     |
| Geometric mean | (ref)                                                  | 1.66x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                    |
| regex_dna      | 220 ms                                                 | 220 ms: 1.00x slower                                                     |
| regex_v8       | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                    |
| regex_compile  | 131 ms                                                 | 217 ms: 1.65x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 153 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 102 ms                                                 | 114 ms: 1.11x slower                                                     |
| json_loads           | 27.0 us                                                | 31.6 us: 1.17x slower                                                    |
| xml_etree_generate   | 87.0 ms                                                | 110 ms: 1.26x slower                                                     |
| json_dumps           | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                    |
| xml_etree_process    | 60.4 ms                                                | 88.3 ms: 1.46x slower                                                    |
| tomli_loads          | 2.11 sec                                               | 3.22 sec: 1.53x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 408 us: 1.91x slower                                                     |
| pickle_pure_python   | 300 us                                                 | 575 us: 1.91x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.37x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 13.7 ms: 1.30x slower                                                    |
| python_startup_no_site | 6.99 ms                                                | 9.30 ms: 1.33x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 82.4 ms: 1.64x slower                                                    |
| django_template | 34.4 ms                                                | 59.8 ms: 1.74x slower                                                    |
| genshi_text     | 22.9 ms                                                | 39.9 ms: 1.74x slower                                                    |
| mako            | 11.1 ms                                                | 21.1 ms: 1.90x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.75x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 3.81 ms                                                | 3.03 ms: 1.26x faster                                                    |
| create_gc_cycles           | 1.61 ms                                                | 1.38 ms: 1.17x faster                                                    |
| regex_effbot               | 3.88 ms                                                | 3.54 ms: 1.10x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 153 ms: 1.02x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 458 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 184 ms: 1.01x faster                                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                    |
| regex_dna                  | 220 ms                                                 | 220 ms: 1.00x slower                                                     |
| regex_v8                   | 25.3 ms                                                | 26.0 ms: 1.03x slower                                                    |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                     |
| async_tree_none_tg         | 320 ms                                                 | 347 ms: 1.08x slower                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 601 ms: 1.11x slower                                                     |
| pathlib                    | 17.1 ms                                                | 18.9 ms: 1.11x slower                                                    |
| xml_etree_iterparse        | 102 ms                                                 | 114 ms: 1.11x slower                                                     |
| json                       | 5.20 ms                                                | 5.93 ms: 1.14x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.05 sec: 1.14x slower                                                   |
| async_tree_none            | 354 ms                                                 | 406 ms: 1.15x slower                                                     |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 659 ms: 1.15x slower                                                     |
| async_tree_memoization     | 442 ms                                                 | 510 ms: 1.15x slower                                                     |
| mdp                        | 2.74 sec                                               | 3.19 sec: 1.16x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 568 ms: 1.16x slower                                                     |
| json_loads                 | 27.0 us                                                | 31.6 us: 1.17x slower                                                    |
| deepcopy                   | 352 us                                                 | 421 us: 1.19x slower                                                     |
| telco                      | 8.45 ms                                                | 10.2 ms: 1.21x slower                                                    |
| pylint                     | 313 ms                                                 | 392 ms: 1.25x slower                                                     |
| generators                 | 28.8 ms                                                | 36.4 ms: 1.26x slower                                                    |
| xml_etree_generate         | 87.0 ms                                                | 110 ms: 1.26x slower                                                     |
| async_generators           | 433 ms                                                 | 557 ms: 1.29x slower                                                     |
| docutils                   | 2.58 sec                                               | 3.33 sec: 1.29x slower                                                   |
| python_startup             | 10.6 ms                                                | 13.7 ms: 1.30x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                    |
| meteor_contest             | 108 ms                                                 | 141 ms: 1.31x slower                                                     |
| scimark_fft                | 369 ms                                                 | 483 ms: 1.31x slower                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.69 ms: 1.33x slower                                                    |
| python_startup_no_site     | 6.99 ms                                                | 9.30 ms: 1.33x slower                                                    |
| pycparser                  | 1.19 sec                                               | 1.62 sec: 1.35x slower                                                   |
| coverage                   | 83.7 ms                                                | 116 ms: 1.38x slower                                                     |
| deepcopy_reduce            | 3.17 us                                                | 4.39 us: 1.38x slower                                                    |
| deepcopy_memo              | 38.0 us                                                | 53.2 us: 1.40x slower                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 6.57 sec: 1.40x slower                                                   |
| coroutines                 | 22.5 ms                                                | 31.6 ms: 1.40x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 28.7 ms: 1.44x slower                                                    |
| nqueens                    | 80.6 ms                                                | 117 ms: 1.45x slower                                                     |
| xml_etree_process          | 60.4 ms                                                | 88.3 ms: 1.46x slower                                                    |
| 2to3                       | 265 ms                                                 | 395 ms: 1.49x slower                                                     |
| tornado_http               | 91.5 ms                                                | 139 ms: 1.52x slower                                                     |
| tomli_loads                | 2.11 sec                                               | 3.22 sec: 1.53x slower                                                   |
| html5lib                   | 64.5 ms                                                | 98.6 ms: 1.53x slower                                                    |
| sympy_str                  | 274 ms                                                 | 422 ms: 1.54x slower                                                     |
| thrift                     | 796 us                                                 | 1.23 ms: 1.55x slower                                                    |
| crypto_pyaes               | 73.0 ms                                                | 113 ms: 1.56x slower                                                     |
| typing_runtime_protocols   | 159 us                                                 | 251 us: 1.58x slower                                                     |
| fannkuch                   | 381 ms                                                 | 605 ms: 1.59x slower                                                     |
| spectral_norm              | 115 ms                                                 | 183 ms: 1.59x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 171 ms: 1.60x slower                                                     |
| sqlglot_optimize           | 53.9 ms                                                | 86.6 ms: 1.61x slower                                                    |
| sympy_expand               | 462 ms                                                 | 746 ms: 1.61x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 82.4 ms: 1.64x slower                                                    |
| regex_compile              | 131 ms                                                 | 217 ms: 1.65x slower                                                     |
| pyflate                    | 460 ms                                                 | 765 ms: 1.66x slower                                                     |
| richards                   | 48.1 ms                                                | 80.1 ms: 1.66x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 256 ms: 1.71x slower                                                     |
| pprint_safe_repr           | 744 ms                                                 | 1.28 sec: 1.73x slower                                                   |
| django_template            | 34.4 ms                                                | 59.8 ms: 1.74x slower                                                    |
| genshi_text                | 22.9 ms                                                | 39.9 ms: 1.74x slower                                                    |
| comprehensions             | 16.4 us                                                | 28.8 us: 1.75x slower                                                    |
| pprint_pformat             | 1.51 sec                                               | 2.66 sec: 1.76x slower                                                   |
| float                      | 78.5 ms                                                | 139 ms: 1.77x slower                                                     |
| richards_super             | 54.4 ms                                                | 97.2 ms: 1.79x slower                                                    |
| logging_simple             | 5.66 us                                                | 10.4 us: 1.84x slower                                                    |
| logging_format             | 6.25 us                                                | 11.7 us: 1.87x slower                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 125 ms: 1.89x slower                                                     |
| mako                       | 11.1 ms                                                | 21.1 ms: 1.90x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 408 us: 1.91x slower                                                     |
| pickle_pure_python         | 300 us                                                 | 575 us: 1.91x slower                                                     |
| logging_silent             | 102 ns                                                 | 197 ns: 1.93x slower                                                     |
| hexiom                     | 6.13 ms                                                | 12.0 ms: 1.96x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 3.10 ms: 1.97x slower                                                    |
| scimark_lu                 | 115 ms                                                 | 238 ms: 2.07x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 2.63 ms: 2.08x slower                                                    |
| chaos                      | 58.4 ms                                                | 125 ms: 2.14x slower                                                     |
| go                         | 142 ms                                                 | 309 ms: 2.19x slower                                                     |
| scimark_sor                | 122 ms                                                 | 268 ms: 2.19x slower                                                     |
| raytrace                   | 262 ms                                                 | 603 ms: 2.30x slower                                                     |
| nbody                      | 85.7 ms                                                | 223 ms: 2.60x slower                                                     |
| deltablue                  | 3.15 ms                                                | 8.38 ms: 2.66x slower                                                    |
| bench_thread_pool          | 815 us                                                 | 3.12 ms: 3.83x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.45x slower                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.16x