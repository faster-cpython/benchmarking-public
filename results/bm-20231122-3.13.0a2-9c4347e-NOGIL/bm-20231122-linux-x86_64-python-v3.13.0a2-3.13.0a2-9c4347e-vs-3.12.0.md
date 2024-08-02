# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 294 ms: 1.07x slower                                       |
| chameleon      | 7.41 ms                                                | 7.76 ms: 1.05x slower                                      |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                     |
| tornado_http   | 103 ms                                                 | 108 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 509 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 804 ms: 1.11x slower                                       |
| async_tree_memoization     | 578 ms                                                 | 657 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 850 ms: 1.17x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 540 ms: 1.20x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.39 sec: 1.20x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 692 ms: 1.20x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.45 sec: 1.23x slower                                     |
| Geometric mean             | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 194 ms: 1.03x slower                                       |
| float          | 84.7 ms                                                | 95.5 ms: 1.13x slower                                      |
| nbody          | 97.0 ms                                                | 110 ms: 1.13x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                       |
| regex_effbot   | 3.61 ms                                                | 3.83 ms: 1.06x slower                                      |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 32.7 us: 1.09x faster                                      |
| pickle_list          | 5.08 us                                                | 4.71 us: 1.08x faster                                      |
| unpickle             | 15.9 us                                                | 15.4 us: 1.03x faster                                      |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.26 us: 1.00x faster                                      |
| tomli_loads          | 2.33 sec                                               | 2.37 sec: 1.02x slower                                     |
| pickle_pure_python   | 324 us                                                 | 335 us: 1.03x slower                                       |
| unpickle_pure_python | 230 us                                                 | 246 us: 1.07x slower                                       |
| xml_etree_iterparse  | 107 ms                                                 | 114 ms: 1.07x slower                                       |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                      |
| json_loads           | 28.5 us                                                | 30.9 us: 1.09x slower                                      |
| xml_etree_parse      | 159 ms                                                 | 472 ms: 2.96x slower                                       |
| xml_etree_process    | 61.7 ms                                                | 1.03 sec: 16.66x slower                                    |
| xml_etree_generate   | 89.2 ms                                                | 1.58 sec: 17.74x slower                                    |
| Geometric mean       | (ref)                                                  | 1.64x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.17x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 9.60 ms: 1.38x slower                                      |
| Geometric mean         | (ref)                                                  | 1.27x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 12.9 ms: 1.09x slower                                      |
| django_template | 34.6 ms                                                | 38.3 ms: 1.11x slower                                      |
| Geometric mean  | (ref)                                                  | 1.10x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 127 us: 1.24x faster                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.22 ms: 1.21x faster                                      |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.18x faster                                      |
| pickle_dict                | 35.5 us                                                | 32.7 us: 1.09x faster                                      |
| pickle_list                | 5.08 us                                                | 4.71 us: 1.08x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 22.6 ms: 1.06x faster                                      |
| gc_traversal               | 3.79 ms                                                | 3.64 ms: 1.04x faster                                      |
| unpickle                   | 15.9 us                                                | 15.4 us: 1.03x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 80.1 ms: 1.02x faster                                      |
| logging_format             | 7.23 us                                                | 7.09 us: 1.02x faster                                      |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| unpickle_list              | 5.29 us                                                | 5.26 us: 1.00x faster                                      |
| raytrace                   | 312 ms                                                 | 314 ms: 1.00x slower                                       |
| regex_compile              | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 76.1 ms: 1.01x slower                                      |
| tomli_loads                | 2.33 sec                                               | 2.37 sec: 1.02x slower                                     |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                       |
| pathlib                    | 19.3 ms                                                | 19.8 ms: 1.02x slower                                      |
| chaos                      | 67.0 ms                                                | 68.7 ms: 1.03x slower                                      |
| pidigits                   | 187 ms                                                 | 194 ms: 1.03x slower                                       |
| dulwich_log                | 68.5 ms                                                | 70.8 ms: 1.03x slower                                      |
| pickle_pure_python         | 324 us                                                 | 335 us: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                     |
| meteor_contest             | 112 ms                                                 | 117 ms: 1.04x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 511 ms: 1.04x slower                                       |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                     |
| chameleon                  | 7.41 ms                                                | 7.76 ms: 1.05x slower                                      |
| pprint_safe_repr           | 776 ms                                                 | 812 ms: 1.05x slower                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                       |
| tornado_http               | 103 ms                                                 | 108 ms: 1.05x slower                                       |
| deepcopy                   | 371 us                                                 | 392 us: 1.06x slower                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.53 us: 1.06x slower                                      |
| pyflate                    | 482 ms                                                 | 510 ms: 1.06x slower                                       |
| deepcopy_memo              | 40.7 us                                                | 43.0 us: 1.06x slower                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                      |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                     |
| regex_effbot               | 3.61 ms                                                | 3.83 ms: 1.06x slower                                      |
| scimark_fft                | 382 ms                                                 | 405 ms: 1.06x slower                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.79 ms: 1.06x slower                                      |
| nqueens                    | 83.3 ms                                                | 88.6 ms: 1.06x slower                                      |
| unpickle_pure_python       | 230 us                                                 | 246 us: 1.07x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 118 ms: 1.07x slower                                       |
| coroutines                 | 23.2 ms                                                | 24.8 ms: 1.07x slower                                      |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                      |
| 2to3                       | 274 ms                                                 | 294 ms: 1.07x slower                                       |
| xml_etree_iterparse        | 107 ms                                                 | 114 ms: 1.07x slower                                       |
| sympy_integrate            | 21.4 ms                                                | 22.9 ms: 1.07x slower                                      |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                       |
| deltablue                  | 3.72 ms                                                | 3.99 ms: 1.07x slower                                      |
| async_tree_none            | 472 ms                                                 | 509 ms: 1.08x slower                                       |
| async_generators           | 463 ms                                                 | 500 ms: 1.08x slower                                       |
| json                       | 5.26 ms                                                | 5.68 ms: 1.08x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.27 sec: 1.08x slower                                     |
| fannkuch                   | 417 ms                                                 | 451 ms: 1.08x slower                                       |
| scimark_sor                | 129 ms                                                 | 140 ms: 1.08x slower                                       |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                      |
| sqlglot_optimize           | 54.8 ms                                                | 59.4 ms: 1.08x slower                                      |
| gunicorn                   | 1.24 ms                                                | 1.35 ms: 1.08x slower                                      |
| json_loads                 | 28.5 us                                                | 30.9 us: 1.09x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.25 ms: 1.09x slower                                      |
| mako                       | 11.9 ms                                                | 12.9 ms: 1.09x slower                                      |
| mdp                        | 2.63 sec                                               | 2.89 sec: 1.10x slower                                     |
| django_template            | 34.6 ms                                                | 38.3 ms: 1.11x slower                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 804 ms: 1.11x slower                                       |
| sympy_str                  | 300 ms                                                 | 332 ms: 1.11x slower                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.61 ms: 1.11x slower                                      |
| logging_silent             | 104 ns                                                 | 116 ns: 1.11x slower                                       |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                      |
| go                         | 139 ms                                                 | 157 ms: 1.12x slower                                       |
| float                      | 84.7 ms                                                | 95.5 ms: 1.13x slower                                      |
| nbody                      | 97.0 ms                                                | 110 ms: 1.13x slower                                       |
| spectral_norm              | 115 ms                                                 | 130 ms: 1.13x slower                                       |
| richards                   | 45.8 ms                                                | 51.9 ms: 1.13x slower                                      |
| async_tree_memoization     | 578 ms                                                 | 657 ms: 1.14x slower                                       |
| sqlite_synth               | 2.83 us                                                | 3.23 us: 1.14x slower                                      |
| richards_super             | 51.5 ms                                                | 59.1 ms: 1.15x slower                                      |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.17x slower                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 850 ms: 1.17x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 540 ms: 1.20x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.39 sec: 1.20x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 692 ms: 1.20x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.45 sec: 1.23x slower                                     |
| sympy_sum                  | 169 ms                                                 | 211 ms: 1.25x slower                                       |
| sympy_expand               | 478 ms                                                 | 613 ms: 1.28x slower                                       |
| bench_thread_pool          | 842 us                                                 | 1.09 ms: 1.29x slower                                      |
| telco                      | 7.10 ms                                                | 9.60 ms: 1.35x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 9.60 ms: 1.38x slower                                      |
| mypy2                      | 830 ms                                                 | 1.15 sec: 1.39x slower                                     |
| xml_etree_parse            | 159 ms                                                 | 472 ms: 2.96x slower                                       |
| coverage                   | 72.7 ms                                                | 725 ms: 9.98x slower                                       |
| xml_etree_process          | 61.7 ms                                                | 1.03 sec: 16.66x slower                                    |
| xml_etree_generate         | 89.2 ms                                                | 1.58 sec: 17.74x slower                                    |
| Geometric mean             | (ref)                                                  | 1.18x slower                                               |

Benchmark hidden because not significant (2): logging_simple, generators
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20231122-3.13.0a2-9c4347e-NOGIL/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.56x