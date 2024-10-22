# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                            |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.0 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 526 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                           |
| float          | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.14x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                           |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.07x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                            |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 526 ms: 1.38x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 865 ms: 1.37x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                           |
| raytrace                   | 312 ms                                                 | 257 ms: 1.22x faster                                                            |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                           |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                           |
| nbody                      | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                           |
| tornado_http               | 103 ms                                                 | 90.0 ms: 1.14x faster                                                           |
| regex_compile              | 148 ms                                                 | 131 ms: 1.14x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 66.7 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                          |
| float                      | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                            |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                           |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                            |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                           |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 788 us: 1.07x faster                                                            |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                           |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                                           |
| dask                       | 372 ms                                                 | 353 ms: 1.05x faster                                                            |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                           |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                          |
| logging_silent             | 104 ns                                                 | 100.0 ns: 1.04x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                            |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                            |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                           |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                          |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                           |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                           |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                           |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                           |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                          |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                            |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                           |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.10 ms: 1.14x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (3): pidigits, bench_mp_pool, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x