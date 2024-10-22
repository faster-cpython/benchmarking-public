# Results vs. 3.12.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 395 ms: 1.44x slower                                                     |
| docutils       | 2.77 sec                                               | 3.33 sec: 1.20x slower                                                   |
| tornado_http   | 103 ms                                                 | 139 ms: 1.36x slower                                                     |
| Geometric mean | (ref)                                                  | 1.33x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.42x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 601 ms: 1.21x faster                                                     |
| async_tree_none            | 472 ms                                                 | 406 ms: 1.16x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 510 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 659 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 184 ms: 1.02x faster                                                     |
| float          | 84.7 ms                                                | 139 ms: 1.64x slower                                                     |
| nbody          | 97.0 ms                                                | 223 ms: 2.30x slower                                                     |
| Geometric mean | (ref)                                                  | 1.55x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                    |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| regex_compile  | 148 ms                                                 | 217 ms: 1.46x slower                                                     |
| Geometric mean | (ref)                                                  | 1.14x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 114 ms: 1.07x slower                                                     |
| json_loads           | 28.5 us                                                | 31.6 us: 1.11x slower                                                    |
| xml_etree_generate   | 89.2 ms                                                | 110 ms: 1.23x slower                                                     |
| json_dumps           | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                    |
| tomli_loads          | 2.33 sec                                               | 3.22 sec: 1.38x slower                                                   |
| xml_etree_process    | 61.7 ms                                                | 88.3 ms: 1.43x slower                                                    |
| pickle_pure_python   | 324 us                                                 | 575 us: 1.77x slower                                                     |
| unpickle_pure_python | 230 us                                                 | 408 us: 1.77x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.31x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.30 ms: 1.34x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.7 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 59.8 ms: 1.73x slower                                                    |
| mako            | 11.9 ms                                                | 21.1 ms: 1.78x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.75x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.42x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 458 ms: 1.26x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.03 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 601 ms: 1.21x faster                                                     |
| async_tree_none            | 472 ms                                                 | 406 ms: 1.16x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 510 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 659 ms: 1.10x faster                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.38 ms: 1.07x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                     |
| pathlib                    | 19.3 ms                                                | 18.9 ms: 1.02x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                    |
| pidigits                   | 187 ms                                                 | 184 ms: 1.02x faster                                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                     |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 114 ms: 1.07x slower                                                     |
| json_loads                 | 28.5 us                                                | 31.6 us: 1.11x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| json                       | 5.26 ms                                                | 5.93 ms: 1.13x slower                                                    |
| deepcopy                   | 371 us                                                 | 421 us: 1.13x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.05 sec: 1.15x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 568 ms: 1.16x slower                                                     |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.16x slower                                                    |
| docutils                   | 2.77 sec                                               | 3.33 sec: 1.20x slower                                                   |
| async_generators           | 463 ms                                                 | 557 ms: 1.20x slower                                                     |
| mdp                        | 2.63 sec                                               | 3.19 sec: 1.21x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 110 ms: 1.23x slower                                                     |
| meteor_contest             | 112 ms                                                 | 141 ms: 1.25x slower                                                     |
| scimark_fft                | 382 ms                                                 | 483 ms: 1.27x slower                                                     |
| deepcopy_memo              | 40.7 us                                                | 53.2 us: 1.31x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 13.6 ms: 1.31x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                | 4.39 us: 1.31x slower                                                    |
| comprehensions             | 21.8 us                                                | 28.8 us: 1.32x slower                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.69 ms: 1.32x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 28.7 ms: 1.34x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 9.30 ms: 1.34x slower                                                    |
| tornado_http               | 103 ms                                                 | 139 ms: 1.36x slower                                                     |
| coroutines                 | 23.2 ms                                                | 31.6 ms: 1.36x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.62 sec: 1.37x slower                                                   |
| tomli_loads                | 2.33 sec                                               | 3.22 sec: 1.38x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 113 ms: 1.39x slower                                                     |
| nqueens                    | 83.3 ms                                                | 117 ms: 1.40x slower                                                     |
| sympy_str                  | 300 ms                                                 | 422 ms: 1.41x slower                                                     |
| xml_etree_process          | 61.7 ms                                                | 88.3 ms: 1.43x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.7 ms: 1.43x slower                                                    |
| telco                      | 7.10 ms                                                | 10.2 ms: 1.44x slower                                                    |
| 2to3                       | 274 ms                                                 | 395 ms: 1.44x slower                                                     |
| fannkuch                   | 417 ms                                                 | 605 ms: 1.45x slower                                                     |
| regex_compile              | 148 ms                                                 | 217 ms: 1.46x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 256 ms: 1.51x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 171 ms: 1.55x slower                                                     |
| sympy_expand               | 478 ms                                                 | 746 ms: 1.56x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 86.6 ms: 1.58x slower                                                    |
| pyflate                    | 482 ms                                                 | 765 ms: 1.59x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 251 us: 1.59x slower                                                     |
| spectral_norm              | 115 ms                                                 | 183 ms: 1.59x slower                                                     |
| coverage                   | 72.7 ms                                                | 116 ms: 1.59x slower                                                     |
| logging_format             | 7.23 us                                                | 11.7 us: 1.61x slower                                                    |
| logging_simple             | 6.46 us                                                | 10.4 us: 1.62x slower                                                    |
| float                      | 84.7 ms                                                | 139 ms: 1.64x slower                                                     |
| pprint_safe_repr           | 776 ms                                                 | 1.28 sec: 1.66x slower                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 125 ms: 1.67x slower                                                     |
| pprint_pformat             | 1.57 sec                                               | 2.66 sec: 1.70x slower                                                   |
| django_template            | 34.6 ms                                                | 59.8 ms: 1.73x slower                                                    |
| richards                   | 45.8 ms                                                | 80.1 ms: 1.75x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 575 us: 1.77x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 408 us: 1.77x slower                                                     |
| mako                       | 11.9 ms                                                | 21.1 ms: 1.78x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 3.10 ms: 1.84x slower                                                    |
| chaos                      | 67.0 ms                                                | 125 ms: 1.87x slower                                                     |
| hexiom                     | 6.41 ms                                                | 12.0 ms: 1.87x slower                                                    |
| richards_super             | 51.5 ms                                                | 97.2 ms: 1.89x slower                                                    |
| logging_silent             | 104 ns                                                 | 197 ns: 1.89x slower                                                     |
| raytrace                   | 312 ms                                                 | 603 ms: 1.93x slower                                                     |
| sqlglot_parse              | 1.36 ms                                                | 2.63 ms: 1.93x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 238 ms: 2.02x slower                                                     |
| scimark_sor                | 129 ms                                                 | 268 ms: 2.07x slower                                                     |
| go                         | 139 ms                                                 | 309 ms: 2.22x slower                                                     |
| deltablue                  | 3.72 ms                                                | 8.38 ms: 2.26x slower                                                    |
| nbody                      | 97.0 ms                                                | 223 ms: 2.30x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 3.12 ms: 3.70x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.36x slower                                                             |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.13x