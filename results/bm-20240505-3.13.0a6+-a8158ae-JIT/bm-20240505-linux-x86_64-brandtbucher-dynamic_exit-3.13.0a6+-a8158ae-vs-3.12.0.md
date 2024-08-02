# Results vs. 3.12.0

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.03x faster
- HPT reliability: 95.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 284 ms: 1.03x slower                                                 |
| chameleon      | 7.41 ms                                                | 7.30 ms: 1.02x faster                                                |
| tornado_http   | 103 ms                                                 | 98.0 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 351 ms: 1.28x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                                 |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 469 ms: 1.23x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 972 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 605 ms: 1.20x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.0 ms: 1.23x faster                                                |
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.19x faster                                               |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 153 ms: 1.04x faster                                                 |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                |
| pickle_list          | 5.08 us                                                | 4.99 us: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                |
| unpickle_list        | 5.29 us                                                | 5.39 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.66 ms: 1.10x slower                                                |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.67 ms: 1.23x faster                                                |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 351 ms: 1.28x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                                 |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 469 ms: 1.23x faster                                                 |
| mako                       | 11.9 ms                                                | 9.67 ms: 1.23x faster                                                |
| nbody                      | 97.0 ms                                                | 79.0 ms: 1.23x faster                                                |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 972 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 605 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.19x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 64.2 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 625 ms: 1.16x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.0 ms: 1.16x faster                                                |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                |
| logging_format             | 7.23 us                                                | 6.43 us: 1.12x faster                                                |
| logging_simple             | 6.46 us                                                | 5.75 us: 1.12x faster                                                |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                                |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 37.8 us: 1.08x faster                                                |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                 |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                 |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                |
| tornado_http               | 103 ms                                                 | 98.0 ms: 1.05x faster                                                |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.05x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 153 ms: 1.04x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                |
| pickle_list                | 5.08 us                                                | 4.99 us: 1.02x faster                                                |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                               |
| chameleon                  | 7.41 ms                                                | 7.30 ms: 1.02x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                                |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                |
| deepcopy                   | 371 us                                                 | 368 us: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                                |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                 |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                 |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                |
| unpickle_list              | 5.29 us                                                | 5.39 us: 1.02x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 70.4 ms: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.60 ms: 1.03x slower                                                |
| 2to3                       | 274 ms                                                 | 284 ms: 1.03x slower                                                 |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                |
| deltablue                  | 3.72 ms                                                | 3.86 ms: 1.04x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 57.0 ms: 1.04x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                               |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                 |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                 |
| nqueens                    | 83.3 ms                                                | 88.4 ms: 1.06x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 521 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                                |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                 |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.12 ms: 1.09x slower                                                |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.09x slower                                                |
| aiohttp                    | 1.15 ms                                                | 1.26 ms: 1.09x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.66 ms: 1.10x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 175 us: 1.11x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                |
| telco                      | 7.10 ms                                                | 8.37 ms: 1.18x slower                                                |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.87 ms: 1.27x slower                                                |
| generators                 | 31.2 ms                                                | 51.4 ms: 1.65x slower                                                |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (4): mypy2, pickle_dict, bench_mp_pool, async_generators
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240505-3.13.0a6+-a8158ae-JIT/bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x