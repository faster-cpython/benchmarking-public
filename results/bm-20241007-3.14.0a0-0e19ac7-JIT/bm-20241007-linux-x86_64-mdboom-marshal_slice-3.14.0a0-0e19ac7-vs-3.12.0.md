# Results vs. 3.12.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                           |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                         |
| tornado_http   | 103 ms                                                 | 94.5 ms: 1.09x faster                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                           |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                           |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                           |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.7 ms: 1.20x faster                                          |
| float          | 84.7 ms                                                | 72.2 ms: 1.17x faster                                          |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                           |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                           |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                          |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 77.2 ms: 1.16x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 54.4 ms: 1.13x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                           |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                          |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                          |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                           |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                           |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.0 ms: 1.04x faster                                          |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                          |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                          |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                          |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.51x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                           |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                           |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                           |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 65.8 ms: 1.24x faster                                          |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                           |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                           |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                         |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                          |
| nbody                      | 97.0 ms                                                | 80.7 ms: 1.20x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 63.3 ms: 1.19x faster                                          |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                          |
| float                      | 84.7 ms                                                | 72.2 ms: 1.17x faster                                          |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 77.2 ms: 1.16x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.42 ms: 1.14x faster                                          |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                          |
| xml_etree_process          | 61.7 ms                                                | 54.4 ms: 1.13x faster                                          |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                           |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                           |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                          |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                           |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                           |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                           |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                          |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                          |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                           |
| tornado_http               | 103 ms                                                 | 94.5 ms: 1.09x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                          |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                          |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                          |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                           |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                           |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                           |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                           |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                         |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                          |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                         |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                           |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                           |
| json_dumps                 | 10.4 ms                                                | 10.0 ms: 1.04x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                          |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                          |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                          |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                         |
| json                       | 5.26 ms                                                | 5.19 ms: 1.01x faster                                          |
| asyncio_tcp                | 491 ms                                                 | 485 ms: 1.01x faster                                           |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                           |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                           |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                          |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                           |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                          |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                          |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                           |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.03x slower                                           |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                          |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                          |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.05x slower                                          |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                           |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                           |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                           |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                         |
| telco                      | 7.10 ms                                                | 7.56 ms: 1.07x slower                                          |
| hexiom                     | 6.41 ms                                                | 6.97 ms: 1.09x slower                                          |
| sympy_integrate            | 21.4 ms                                                | 23.3 ms: 1.09x slower                                          |
| sqlglot_optimize           | 54.8 ms                                                | 60.4 ms: 1.10x slower                                          |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                          |
| generators                 | 31.2 ms                                                | 35.0 ms: 1.12x slower                                          |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                          |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.00x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 61.2 ms: 2.55x slower                                          |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (3): sqlglot_parse, sympy_str, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0e19ac7-JIT/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x