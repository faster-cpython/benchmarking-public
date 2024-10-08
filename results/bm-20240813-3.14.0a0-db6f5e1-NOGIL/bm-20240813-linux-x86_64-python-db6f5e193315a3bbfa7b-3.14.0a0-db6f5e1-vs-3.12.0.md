# Results vs. 3.12.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 395 ms: 1.44x slower                                                  |
| docutils       | 2.77 sec                                               | 3.34 sec: 1.21x slower                                                |
| tornado_http   | 103 ms                                                 | 138 ms: 1.35x slower                                                  |
| Geometric mean | (ref)                                                  | 1.33x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 840 ms: 1.41x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 456 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| async_tree_none            | 472 ms                                                 | 412 ms: 1.15x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 517 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 662 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 184 ms: 1.02x faster                                                  |
| float          | 84.7 ms                                                | 142 ms: 1.67x slower                                                  |
| nbody          | 97.0 ms                                                | 222 ms: 2.29x slower                                                  |
| Geometric mean | (ref)                                                  | 1.56x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.51 ms: 1.03x faster                                                 |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.13x slower                                                 |
| regex_compile  | 148 ms                                                 | 217 ms: 1.47x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 113 ms: 1.06x slower                                                  |
| json_loads           | 28.5 us                                                | 32.4 us: 1.14x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 110 ms: 1.24x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                 |
| tomli_loads          | 2.33 sec                                               | 3.26 sec: 1.40x slower                                                |
| xml_etree_process    | 61.7 ms                                                | 88.8 ms: 1.44x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 572 us: 1.76x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 411 us: 1.79x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.31 ms: 1.34x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.7 ms: 1.44x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 59.2 ms: 1.71x slower                                                 |
| mako            | 11.9 ms                                                | 21.0 ms: 1.76x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.74x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 840 ms: 1.41x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 456 ms: 1.26x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.02 ms: 1.26x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.21x faster                                                  |
| async_tree_none            | 472 ms                                                 | 412 ms: 1.15x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 517 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 662 ms: 1.10x faster                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.38 ms: 1.07x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.51 ms: 1.03x faster                                                 |
| pidigits                   | 187 ms                                                 | 184 ms: 1.02x faster                                                  |
| pathlib                    | 19.3 ms                                                | 19.2 ms: 1.01x faster                                                 |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 113 ms: 1.06x slower                                                  |
| deepcopy                   | 371 us                                                 | 417 us: 1.12x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.13x slower                                                 |
| json_loads                 | 28.5 us                                                | 32.4 us: 1.14x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 561 ms: 1.14x slower                                                  |
| json                       | 5.26 ms                                                | 6.04 ms: 1.15x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.16x slower                                                |
| generators                 | 31.2 ms                                                | 37.4 ms: 1.20x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.34 sec: 1.21x slower                                                |
| async_generators           | 463 ms                                                 | 559 ms: 1.21x slower                                                  |
| mdp                        | 2.63 sec                                               | 3.21 sec: 1.22x slower                                                |
| xml_etree_generate         | 89.2 ms                                                | 110 ms: 1.24x slower                                                  |
| scimark_fft                | 382 ms                                                 | 484 ms: 1.27x slower                                                  |
| meteor_contest             | 112 ms                                                 | 143 ms: 1.27x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 4.28 us: 1.28x slower                                                 |
| deepcopy_memo              | 40.7 us                                                | 52.2 us: 1.28x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                 |
| comprehensions             | 21.8 us                                                | 28.8 us: 1.32x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 9.31 ms: 1.34x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 28.8 ms: 1.34x slower                                                 |
| tornado_http               | 103 ms                                                 | 138 ms: 1.35x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.95 ms: 1.37x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.63 sec: 1.38x slower                                                |
| crypto_pyaes               | 81.9 ms                                                | 113 ms: 1.38x slower                                                  |
| coroutines                 | 23.2 ms                                                | 32.1 ms: 1.39x slower                                                 |
| tomli_loads                | 2.33 sec                                               | 3.26 sec: 1.40x slower                                                |
| sympy_str                  | 300 ms                                                 | 425 ms: 1.42x slower                                                  |
| nqueens                    | 83.3 ms                                                | 119 ms: 1.43x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.7 ms: 1.44x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 88.8 ms: 1.44x slower                                                 |
| 2to3                       | 274 ms                                                 | 395 ms: 1.44x slower                                                  |
| telco                      | 7.10 ms                                                | 10.4 ms: 1.46x slower                                                 |
| regex_compile              | 148 ms                                                 | 217 ms: 1.47x slower                                                  |
| fannkuch                   | 417 ms                                                 | 625 ms: 1.50x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 256 ms: 1.51x slower                                                  |
| coverage                   | 72.7 ms                                                | 111 ms: 1.53x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 171 ms: 1.55x slower                                                  |
| sympy_expand               | 478 ms                                                 | 748 ms: 1.56x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 85.9 ms: 1.57x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 249 us: 1.57x slower                                                  |
| logging_simple             | 6.46 us                                                | 10.3 us: 1.60x slower                                                 |
| pyflate                    | 482 ms                                                 | 773 ms: 1.60x slower                                                  |
| logging_format             | 7.23 us                                                | 11.6 us: 1.60x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.27 sec: 1.64x slower                                                |
| spectral_norm              | 115 ms                                                 | 189 ms: 1.64x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 124 ms: 1.66x slower                                                  |
| float                      | 84.7 ms                                                | 142 ms: 1.67x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.64 sec: 1.68x slower                                                |
| richards                   | 45.8 ms                                                | 78.3 ms: 1.71x slower                                                 |
| django_template            | 34.6 ms                                                | 59.2 ms: 1.71x slower                                                 |
| mako                       | 11.9 ms                                                | 21.0 ms: 1.76x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 572 us: 1.76x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 411 us: 1.79x slower                                                  |
| logging_silent             | 104 ns                                                 | 191 ns: 1.83x slower                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 3.08 ms: 1.83x slower                                                 |
| richards_super             | 51.5 ms                                                | 95.4 ms: 1.85x slower                                                 |
| chaos                      | 67.0 ms                                                | 125 ms: 1.87x slower                                                  |
| hexiom                     | 6.41 ms                                                | 12.0 ms: 1.88x slower                                                 |
| raytrace                   | 312 ms                                                 | 598 ms: 1.92x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 2.63 ms: 1.93x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 240 ms: 2.04x slower                                                  |
| scimark_sor                | 129 ms                                                 | 266 ms: 2.06x slower                                                  |
| go                         | 139 ms                                                 | 306 ms: 2.19x slower                                                  |
| deltablue                  | 3.72 ms                                                | 8.34 ms: 2.24x slower                                                 |
| nbody                      | 97.0 ms                                                | 222 ms: 2.29x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.11 ms: 3.70x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.36x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-db6f5e1-NOGIL/bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.13x