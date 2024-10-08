# Results vs. 3.12.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| tornado_http   | 103 ms                                                 | 90.0 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 287 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 370 ms: 1.55x faster                                                   |
| async_tree_none            | 472 ms                                                 | 318 ms: 1.48x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.42x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 820 ms: 1.41x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.44x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                  |
| float          | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                  |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.09x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 287 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 370 ms: 1.55x faster                                                   |
| async_tree_none            | 472 ms                                                 | 318 ms: 1.48x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 400 ms: 1.44x faster                                                   |
| deepcopy                   | 371 us                                                 | 259 us: 1.44x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 830 ms: 1.42x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 820 ms: 1.41x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                   |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                  |
| tornado_http               | 103 ms                                                 | 90.0 ms: 1.14x faster                                                  |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 66.4 ms: 1.13x faster                                                  |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                   |
| float                      | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.59 ms: 1.10x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.09x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.53 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 786 us: 1.07x faster                                                   |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.4 ms: 1.06x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.1 ms: 1.05x faster                                                  |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                 |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                   |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                   |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                   |
| richards                   | 45.8 ms                                                | 46.6 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                   |
| richards_super             | 51.5 ms                                                | 53.1 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 91.7 ms: 1.26x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_tcp_ssl, coroutines, scimark_sor
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x