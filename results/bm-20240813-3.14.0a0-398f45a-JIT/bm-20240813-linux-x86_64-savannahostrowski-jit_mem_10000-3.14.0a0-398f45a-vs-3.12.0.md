# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_mem_10000
- machine: linux-x86_64
- commit hash: 398f45a
- commit date: 2024-08-13
- overall geometric mean: 1.07x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 301 ms: 1.10x slower                                                      |
| docutils       | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                    |
| tornado_http   | 103 ms                                                 | 95.6 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 837 ms: 1.41x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                     |
| float          | 84.7 ms                                                | 74.6 ms: 1.13x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                      |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.20x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                     |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.53x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 402 ms: 1.43x faster                                                      |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 837 ms: 1.41x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                     |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                     |
| mako                       | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.20x faster                                                    |
| nbody                      | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| float                      | 84.7 ms                                                | 74.6 ms: 1.13x faster                                                     |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                                     |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                     |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                      |
| richards_super             | 51.5 ms                                                | 46.3 ms: 1.11x faster                                                     |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                                      |
| tornado_http               | 103 ms                                                 | 95.6 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                      |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 823 us: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                    |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                     |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                    |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                      |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.06x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.80 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                      |
| 2to3                       | 274 ms                                                 | 301 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 61.0 ms: 1.11x slower                                                     |
| generators                 | 31.2 ms                                                | 35.2 ms: 1.13x slower                                                     |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-398f45a-JIT/bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x