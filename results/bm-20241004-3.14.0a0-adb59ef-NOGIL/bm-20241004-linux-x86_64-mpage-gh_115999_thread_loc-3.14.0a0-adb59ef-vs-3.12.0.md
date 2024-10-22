# Results vs. 3.12.0

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.33x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 393 ms: 1.43x slower                                                 |
| docutils       | 2.77 sec                                               | 3.24 sec: 1.17x slower                                               |
| tornado_http   | 103 ms                                                 | 138 ms: 1.35x slower                                                 |
| Geometric mean | (ref)                                                  | 1.31x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 836 ms: 1.41x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 356 ms: 1.26x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 603 ms: 1.20x faster                                                 |
| async_tree_none            | 472 ms                                                 | 402 ms: 1.17x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 505 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 656 ms: 1.11x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 183 ms: 1.02x faster                                                 |
| float          | 84.7 ms                                                | 137 ms: 1.62x slower                                                 |
| nbody          | 97.0 ms                                                | 189 ms: 1.95x slower                                                 |
| Geometric mean | (ref)                                                  | 1.46x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                |
| regex_compile  | 148 ms                                                 | 213 ms: 1.43x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle               | 11.6 us                                                | 10.7 us: 1.08x faster                                                |
| pickle_dict          | 35.5 us                                                | 33.0 us: 1.08x faster                                                |
| pickle_list          | 5.08 us                                                | 4.75 us: 1.07x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.49 us: 1.04x slower                                                |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.05x slower                                                 |
| json_loads           | 28.5 us                                                | 30.3 us: 1.06x slower                                                |
| xml_etree_generate   | 89.2 ms                                                | 108 ms: 1.22x slower                                                 |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.24x slower                                                |
| tomli_loads          | 2.33 sec                                               | 3.17 sec: 1.36x slower                                               |
| xml_etree_process    | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                |
| unpickle_pure_python | 230 us                                                 | 390 us: 1.69x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 564 us: 1.74x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.52 ms: 1.37x slower                                                |
| python_startup         | 9.55 ms                                                | 14.3 ms: 1.49x slower                                                |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 59.7 ms: 1.72x slower                                                |
| mako            | 11.9 ms                                                | 20.7 ms: 1.74x slower                                                |
| Geometric mean  | (ref)                                                  | 1.73x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 836 ms: 1.41x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 2.90 ms: 1.31x faster                                                |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 356 ms: 1.26x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 603 ms: 1.20x faster                                                 |
| async_tree_none            | 472 ms                                                 | 402 ms: 1.17x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 505 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 656 ms: 1.11x faster                                                 |
| pickle                     | 11.6 us                                                | 10.7 us: 1.08x faster                                                |
| pickle_dict                | 35.5 us                                                | 33.0 us: 1.08x faster                                                |
| pickle_list                | 5.08 us                                                | 4.75 us: 1.07x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.39 ms: 1.06x faster                                                |
| pidigits                   | 187 ms                                                 | 183 ms: 1.02x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                |
| pathlib                    | 19.3 ms                                                | 19.1 ms: 1.01x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                 |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.49 us: 1.04x slower                                                |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 30.3 us: 1.06x slower                                                |
| json                       | 5.26 ms                                                | 5.60 ms: 1.06x slower                                                |
| deepcopy                   | 371 us                                                 | 408 us: 1.10x slower                                                 |
| scimark_fft                | 382 ms                                                 | 422 ms: 1.10x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.14 us: 1.11x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 558 ms: 1.14x slower                                                 |
| async_generators           | 463 ms                                                 | 531 ms: 1.15x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.16x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.88 ms: 1.16x slower                                                |
| docutils                   | 2.77 sec                                               | 3.24 sec: 1.17x slower                                               |
| xml_etree_generate         | 89.2 ms                                                | 108 ms: 1.22x slower                                                 |
| generators                 | 31.2 ms                                                | 38.0 ms: 1.22x slower                                                |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.24x slower                                                |
| meteor_contest             | 112 ms                                                 | 141 ms: 1.25x slower                                                 |
| mdp                        | 2.63 sec                                               | 3.32 sec: 1.26x slower                                               |
| deepcopy_memo              | 40.7 us                                                | 51.4 us: 1.26x slower                                                |
| deepcopy_reduce            | 3.35 us                                                | 4.23 us: 1.27x slower                                                |
| dulwich_log                | 68.5 ms                                                | 87.6 ms: 1.28x slower                                                |
| coroutines                 | 23.2 ms                                                | 30.1 ms: 1.30x slower                                                |
| comprehensions             | 21.8 us                                                | 28.4 us: 1.30x slower                                                |
| tornado_http               | 103 ms                                                 | 138 ms: 1.35x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 110 ms: 1.35x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.60 sec: 1.36x slower                                               |
| tomli_loads                | 2.33 sec                                               | 3.17 sec: 1.36x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 9.52 ms: 1.37x slower                                                |
| nqueens                    | 83.3 ms                                                | 114 ms: 1.37x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 29.4 ms: 1.37x slower                                                |
| telco                      | 7.10 ms                                                | 9.92 ms: 1.40x slower                                                |
| fannkuch                   | 417 ms                                                 | 585 ms: 1.40x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                |
| spectral_norm              | 115 ms                                                 | 163 ms: 1.42x slower                                                 |
| sympy_str                  | 300 ms                                                 | 429 ms: 1.43x slower                                                 |
| 2to3                       | 274 ms                                                 | 393 ms: 1.43x slower                                                 |
| regex_compile              | 148 ms                                                 | 213 ms: 1.43x slower                                                 |
| coverage                   | 72.7 ms                                                | 108 ms: 1.49x slower                                                 |
| python_startup             | 9.55 ms                                                | 14.3 ms: 1.49x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 168 ms: 1.53x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 84.5 ms: 1.54x slower                                                |
| logging_format             | 7.23 us                                                | 11.2 us: 1.55x slower                                                |
| pyflate                    | 482 ms                                                 | 751 ms: 1.56x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 246 us: 1.56x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 117 ms: 1.56x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 265 ms: 1.57x slower                                                 |
| logging_simple             | 6.46 us                                                | 10.2 us: 1.58x slower                                                |
| sympy_expand               | 478 ms                                                 | 758 ms: 1.59x slower                                                 |
| float                      | 84.7 ms                                                | 137 ms: 1.62x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.25 sec: 1.62x slower                                               |
| pprint_pformat             | 1.57 sec                                               | 2.58 sec: 1.64x slower                                               |
| chaos                      | 67.0 ms                                                | 112 ms: 1.67x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 390 us: 1.69x slower                                                 |
| richards                   | 45.8 ms                                                | 78.0 ms: 1.70x slower                                                |
| django_template            | 34.6 ms                                                | 59.7 ms: 1.72x slower                                                |
| mako                       | 11.9 ms                                                | 20.7 ms: 1.74x slower                                                |
| pickle_pure_python         | 324 us                                                 | 564 us: 1.74x slower                                                 |
| raytrace                   | 312 ms                                                 | 564 ms: 1.81x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 3.07 ms: 1.82x slower                                                |
| hexiom                     | 6.41 ms                                                | 11.7 ms: 1.83x slower                                                |
| richards_super             | 51.5 ms                                                | 95.6 ms: 1.86x slower                                                |
| logging_silent             | 104 ns                                                 | 195 ns: 1.87x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 221 ms: 1.88x slower                                                 |
| sqlglot_parse              | 1.36 ms                                                | 2.60 ms: 1.91x slower                                                |
| go                         | 139 ms                                                 | 267 ms: 1.91x slower                                                 |
| scimark_sor                | 129 ms                                                 | 251 ms: 1.94x slower                                                 |
| nbody                      | 97.0 ms                                                | 189 ms: 1.95x slower                                                 |
| deltablue                  | 3.72 ms                                                | 8.21 ms: 2.21x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 66.3 ms: 2.76x slower                                                |
| unpack_sequence            | 54.0 ns                                                | 150 ns: 2.79x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 3.44 ms: 4.09x slower                                                |
| Geometric mean             | (ref)                                                  | 1.33x slower                                                         |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-adb59ef-NOGIL/bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: 1.14x