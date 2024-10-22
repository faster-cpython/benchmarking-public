# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_122821
- machine: linux-x86_64
- commit hash: 87e2bf8
- commit date: 2024-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                |
| tornado_http   | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                 |
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                 |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                 |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                 |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.8 ms: 1.13x faster                                                 |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.12x faster                                                 |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                 |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.54 ms: 1.07x faster                                                 |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 791 us: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                 |
| logging_silent             | 104 ns                                                 | 99.2 ns: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 443 ms: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                  |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                  |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                 |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| pyflate                    | 482 ms                                                 | 478 ms: 1.01x faster                                                  |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 492 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                  |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                 |
| telco                      | 7.10 ms                                                | 8.26 ms: 1.16x slower                                                 |
| coverage                   | 72.7 ms                                                | 90.8 ms: 1.25x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): bench_mp_pool, spectral_norm, json_dumps, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240812-3.14.0a0-87e2bf8/bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.97x