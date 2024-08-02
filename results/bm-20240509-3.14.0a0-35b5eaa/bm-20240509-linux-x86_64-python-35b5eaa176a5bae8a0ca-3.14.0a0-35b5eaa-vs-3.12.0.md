# Results vs. 3.12.0

- fork: python
- ref: 35b5eaa176a5bae8a0ca
- machine: linux-x86_64
- commit hash: 35b5eaa
- commit date: 2024-05-09
- overall geometric mean: 1.00x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                  |
| chameleon      | 7.41 ms                                                | 6.87 ms: 1.08x faster                                                 |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                |
| tornado_http   | 103 ms                                                 | 93.7 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 361 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 983 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 618 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| nbody          | 97.0 ms                                                | 88.6 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                 |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                                 |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.47 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_none            | 472 ms                                                 | 361 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 983 ms: 1.20x faster                                                  |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 618 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                 |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                 |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| tornado_http               | 103 ms                                                 | 93.7 ms: 1.10x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.6 ms: 1.09x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| chameleon                  | 7.41 ms                                                | 6.87 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                  |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                 |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                  |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.62 ms: 1.05x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                 |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 87.4 ms: 1.02x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                 |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                  |
| deepcopy                   | 371 us                                                 | 366 us: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                  |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 766 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 832 us: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                                 |
| bench_mp_pool              | 24.0 ms                                                | 23.7 ms: 1.01x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.00x faster                                                  |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                                 |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.01x slower                                                |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.17 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                  |
| json                       | 5.26 ms                                                | 5.44 ms: 1.03x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.47 us: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                                 |
| richards                   | 45.8 ms                                                | 47.9 ms: 1.04x slower                                                 |
| richards_super             | 51.5 ms                                                | 53.8 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.28x slower                                                 |
| telco                      | 7.10 ms                                                | 176 ms: 24.82x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (7): dask, spectral_norm, xml_etree_iterparse, pprint_pformat, sqlglot_optimize, mdp, unpickle
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240509-3.14.0a0-35b5eaa/bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x