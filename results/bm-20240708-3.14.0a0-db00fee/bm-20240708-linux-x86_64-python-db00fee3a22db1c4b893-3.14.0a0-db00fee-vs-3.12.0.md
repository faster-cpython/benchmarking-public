# Results vs. 3.12.0

- fork: python
- ref: db00fee3a22db1c4b893
- machine: linux-x86_64
- commit hash: db00fee
- commit date: 2024-07-08
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| tornado_http   | 103 ms                                                 | 90.6 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 836 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                 |
| float          | 84.7 ms                                                | 76.3 ms: 1.11x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 377 ms: 1.52x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 836 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| tornado_http               | 103 ms                                                 | 90.6 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                |
| float                      | 84.7 ms                                                | 76.3 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.10x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.51 ms: 1.08x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                 |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.4 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                 |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                 |
| logging_silent             | 104 ns                                                 | 99.7 ns: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                 |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                  |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                |
| dask                       | 372 ms                                                 | 358 ms: 1.04x faster                                                  |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 474 ms: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| go                         | 139 ms                                                 | 139 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                  |
| richards                   | 45.8 ms                                                | 46.3 ms: 1.01x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.13 ms: 1.15x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): django_template, xml_etree_parse, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240708-3.14.0a0-db00fee/bm-20240708-linux-x86_64-python-db00fee3a22db1c4b893-3.14.0a0-db00fee.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x