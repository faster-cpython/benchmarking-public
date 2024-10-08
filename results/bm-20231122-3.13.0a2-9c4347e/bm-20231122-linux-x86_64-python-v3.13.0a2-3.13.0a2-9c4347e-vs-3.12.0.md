# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x faster
- HPT reliability: 83.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                       |
| chameleon      | 7.41 ms                                                | 6.93 ms: 1.07x faster                                      |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                     |
| tornado_http   | 103 ms                                                 | 97.6 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 451 ms: 1.05x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 471 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                     |
| async_tree_io_tg           | 1.18 sec                                               | 1.26 sec: 1.07x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 618 ms: 1.08x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 91.0 ms: 1.07x faster                                      |
| float          | 84.7 ms                                                | 83.5 ms: 1.01x faster                                      |
| pidigits       | 187 ms                                                 | 197 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.57 ms: 1.01x faster                                      |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.23 sec: 1.05x faster                                     |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                       |
| unpickle_list        | 5.29 us                                                | 5.12 us: 1.03x faster                                      |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.03x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 88.2 ms: 1.01x faster                                      |
| unpickle             | 15.9 us                                                | 15.7 us: 1.01x faster                                      |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 9.26 ms: 1.34x slower                                      |
| Geometric mean         | (ref)                                                  | 1.22x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                      |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 119 us: 1.33x faster                                       |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                      |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                       |
| logging_format             | 7.23 us                                                | 6.50 us: 1.11x faster                                      |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                       |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                       |
| logging_simple             | 6.46 us                                                | 5.89 us: 1.10x faster                                      |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 70.0 ms: 1.07x faster                                      |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                      |
| chameleon                  | 7.41 ms                                                | 6.93 ms: 1.07x faster                                      |
| nbody                      | 97.0 ms                                                | 91.0 ms: 1.07x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.14 us: 1.06x faster                                      |
| coroutines                 | 23.2 ms                                                | 21.8 ms: 1.06x faster                                      |
| chaos                      | 67.0 ms                                                | 63.4 ms: 1.06x faster                                      |
| tornado_http               | 103 ms                                                 | 97.6 ms: 1.05x faster                                      |
| deepcopy                   | 371 us                                                 | 354 us: 1.05x faster                                       |
| tomli_loads                | 2.33 sec                                               | 2.23 sec: 1.05x faster                                     |
| async_tree_none            | 472 ms                                                 | 451 ms: 1.05x faster                                       |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                       |
| pathlib                    | 19.3 ms                                                | 18.6 ms: 1.04x faster                                      |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                       |
| generators                 | 31.2 ms                                                | 30.1 ms: 1.04x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                      |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                       |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                       |
| unpickle_list              | 5.29 us                                                | 5.12 us: 1.03x faster                                      |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                     |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                      |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.03x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 39.8 us: 1.02x faster                                      |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                      |
| scimark_fft                | 382 ms                                                 | 375 ms: 1.02x faster                                       |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                       |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.02x faster                                      |
| float                      | 84.7 ms                                                | 83.5 ms: 1.01x faster                                      |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                       |
| regex_effbot               | 3.61 ms                                                | 3.57 ms: 1.01x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 88.2 ms: 1.01x faster                                      |
| unpickle                   | 15.9 us                                                | 15.7 us: 1.01x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.3 ms: 1.01x faster                                      |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                       |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                       |
| mdp                        | 2.63 sec                                               | 2.64 sec: 1.00x slower                                     |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.48 ms: 1.01x slower                                      |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                     |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                       |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.02x slower                                      |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                       |
| aiohttp                    | 1.15 ms                                                | 1.17 ms: 1.02x slower                                      |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                      |
| gunicorn                   | 1.24 ms                                                | 1.27 ms: 1.02x slower                                      |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                       |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 471 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                       |
| pidigits                   | 187 ms                                                 | 197 ms: 1.05x slower                                       |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                     |
| async_tree_io_tg           | 1.18 sec                                               | 1.26 sec: 1.07x slower                                     |
| richards_super             | 51.5 ms                                                | 55.1 ms: 1.07x slower                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 618 ms: 1.08x slower                                       |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                      |
| richards                   | 45.8 ms                                                | 49.7 ms: 1.08x slower                                      |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.37 ms: 1.15x slower                                      |
| telco                      | 7.10 ms                                                | 8.53 ms: 1.20x slower                                      |
| coverage                   | 72.7 ms                                                | 95.2 ms: 1.31x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 9.26 ms: 1.34x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (7): json, bench_mp_pool, pickle_list, nqueens, async_tree_memoization, async_tree_cpu_io_mixed, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x