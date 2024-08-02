# Results vs. 3.12.0

- fork: faster-cpython
- ref: test_perf_jit
- machine: linux-x86_64
- commit hash: 1973514
- commit date: 2024-05-10
- overall geometric mean: 1.00x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.02x faster                                                     |
| chameleon      | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                    |
| docutils       | 2.77 sec                                               | 2.81 sec: 1.01x slower                                                   |
| tornado_http   | 103 ms                                                 | 94.5 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 989 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                    |
| nbody          | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                    |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.0 us: 1.05x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                     |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                                    |
| xml_etree_generate   | 89.2 ms                                                | 89.5 ms: 1.00x slower                                                    |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                     |
| unpickle             | 15.9 us                                                | 16.2 us: 1.02x slower                                                    |
| unpickle_list        | 5.29 us                                                | 5.48 us: 1.04x slower                                                    |
| pickle_list          | 5.08 us                                                | 5.63 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                    |
| django_template | 34.6 ms                                                | 35.1 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                    |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 457 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 935 ms: 1.24x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 479 ms: 1.21x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 989 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                     |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                   |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                    |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                    |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                    |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.5 ms: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                     |
| nbody                      | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                    |
| chameleon                  | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                    |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                    |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                    |
| pickle_dict                | 35.5 us                                                | 34.0 us: 1.05x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 65.9 ms: 1.04x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.22 us: 1.04x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                     |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                     |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                    |
| deepcopy                   | 371 us                                                 | 364 us: 1.02x faster                                                     |
| nqueens                    | 83.3 ms                                                | 81.9 ms: 1.02x faster                                                    |
| 2to3                       | 274 ms                                                 | 270 ms: 1.02x faster                                                     |
| scimark_fft                | 382 ms                                                 | 377 ms: 1.01x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                     |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                     |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 771 ms: 1.01x faster                                                     |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                                    |
| xml_etree_generate         | 89.2 ms                                                | 89.5 ms: 1.00x slower                                                    |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 55.2 ms: 1.01x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                    |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                     |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.12 ms: 1.01x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.81 sec: 1.01x slower                                                   |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.02x slower                                                    |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                     |
| unpickle                   | 15.9 us                                                | 16.2 us: 1.02x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                    |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                    |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| unpickle_list              | 5.29 us                                                | 5.48 us: 1.04x slower                                                    |
| richards                   | 45.8 ms                                                | 47.8 ms: 1.04x slower                                                    |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                                    |
| richards_super             | 51.5 ms                                                | 54.2 ms: 1.05x slower                                                    |
| json                       | 5.26 ms                                                | 5.53 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                    |
| pickle_list                | 5.08 us                                                | 5.63 us: 1.11x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                    |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.27x slower                                                    |
| telco                      | 7.10 ms                                                | 177 ms: 24.89x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (7): dask, pycparser, xml_etree_iterparse, pprint_pformat, coroutines, xml_etree_process, sqlglot_normalize
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240510-3.14.0a0-1973514/bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x