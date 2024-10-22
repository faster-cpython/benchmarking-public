# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                |
| tornado_http   | 103 ms                                                 | 92.1 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                  |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 844 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 75.6 ms: 1.28x faster                                                 |
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 81.7 ms: 1.09x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                 |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 27.9 us: 1.46x faster                                                 |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 844 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| nbody                      | 97.0 ms                                                | 75.6 ms: 1.28x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.6 ms: 1.24x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                 |
| mako                       | 11.9 ms                                                | 9.73 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                                |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                 |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| logging_format             | 7.23 us                                                | 5.99 us: 1.21x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                 |
| richards                   | 45.8 ms                                                | 40.5 ms: 1.13x faster                                                 |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.13x faster                                                 |
| pyflate                    | 482 ms                                                 | 429 ms: 1.12x faster                                                  |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| tornado_http               | 103 ms                                                 | 92.1 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                 |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                  |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 81.7 ms: 1.09x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                 |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.04x faster                                                  |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                 |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                  |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                 |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.45 ms: 1.01x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 21.7 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.02x slower                                                  |
| sympy_expand               | 478 ms                                                 | 488 ms: 1.02x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                 |
| nqueens                    | 83.3 ms                                                | 86.2 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                  |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.23 ms: 1.16x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                 |
| coverage                   | 72.7 ms                                                | 92.5 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): bench_mp_pool, sqlglot_optimize, coroutines, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x