# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.03x faster
- HPT reliability: 87.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                            |
| chameleon      | 7.41 ms                                                | 7.12 ms: 1.04x faster                                                           |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                          |
| tornado_http   | 103 ms                                                 | 97.1 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                            |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 965 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 620 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                           |
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                           |
| regex_dna      | 212 ms                                                 | 233 ms: 1.10x slower                                                            |
| regex_v8       | 23.1 ms                                                | 26.5 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                            |
| unpickle             | 15.9 us                                                | 15.2 us: 1.05x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                           |
| pickle               | 11.6 us                                                | 12.0 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                           |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 335 ms: 1.34x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                           |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                           |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 965 ms: 1.20x faster                                                            |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 620 ms: 1.17x faster                                                            |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                           |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                           |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                                            |
| scimark_fft                | 382 ms                                                 | 334 ms: 1.14x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                           |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.09x faster                                                            |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                            |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                          |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                            |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 38.5 us: 1.06x faster                                                           |
| tornado_http               | 103 ms                                                 | 97.1 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                                           |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.05x faster                                                           |
| chameleon                  | 7.41 ms                                                | 7.12 ms: 1.04x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                           |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                                           |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.01x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                           |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                            |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| dulwich_log                | 68.5 ms                                                | 69.4 ms: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                           |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                            |
| deltablue                  | 3.72 ms                                                | 3.79 ms: 1.02x slower                                                           |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                                           |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 865 us: 1.03x slower                                                            |
| hexiom                     | 6.41 ms                                                | 6.60 ms: 1.03x slower                                                           |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                            |
| pickle                     | 11.6 us                                                | 12.0 us: 1.03x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.8 ms: 1.04x slower                                                           |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                          |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                           |
| nqueens                    | 83.3 ms                                                | 87.2 ms: 1.05x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 519 ms: 1.06x slower                                                            |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                           |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.08 ms: 1.08x slower                                                           |
| sympy_expand               | 478 ms                                                 | 514 ms: 1.08x slower                                                            |
| go                         | 139 ms                                                 | 151 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                           |
| regex_dna                  | 212 ms                                                 | 233 ms: 1.10x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 26.5 ms: 1.15x slower                                                           |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                                           |
| coverage                   | 72.7 ms                                                | 93.8 ms: 1.29x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (8): deepcopy, generators, json, async_generators, bench_mp_pool, mdp, unpickle_list, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-881df50-JIT/bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 87.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x