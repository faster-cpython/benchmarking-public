# Results vs. 3.12.0

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 357 ms: 1.30x slower                                                 |
| chameleon      | 7.41 ms                                                | 9.02 ms: 1.22x slower                                                |
| tornado_http   | 103 ms                                                 | 108 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.19x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 481 ms: 1.19x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 379 ms: 1.19x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.03 sec: 1.15x faster                                               |
| async_tree_none            | 472 ms                                                 | 411 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 639 ms: 1.14x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 1.05 sec: 1.10x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 666 ms: 1.09x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 532 ms: 1.08x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                 |
| float          | 84.7 ms                                                | 92.6 ms: 1.09x slower                                                |
| nbody          | 97.0 ms                                                | 123 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                 |
| regex_v8       | 23.1 ms                                                | 27.1 ms: 1.17x slower                                                |
| regex_compile  | 148 ms                                                 | 220 ms: 1.48x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                                |
| pickle_list          | 5.08 us                                                | 5.03 us: 1.01x faster                                                |
| pickle_dict          | 35.5 us                                                | 36.0 us: 1.01x slower                                                |
| xml_etree_iterparse  | 107 ms                                                 | 111 ms: 1.04x slower                                                 |
| pickle               | 11.6 us                                                | 12.1 us: 1.05x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| xml_etree_process    | 61.7 ms                                                | 71.4 ms: 1.16x slower                                                |
| xml_etree_generate   | 89.2 ms                                                | 104 ms: 1.16x slower                                                 |
| tomli_loads          | 2.33 sec                                               | 2.81 sec: 1.21x slower                                               |
| unpickle_pure_python | 230 us                                                 | 331 us: 1.44x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 525 us: 1.62x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.25 ms: 1.05x slower                                                |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 14.2 ms: 1.19x slower                                                |
| django_template | 34.6 ms                                                | 49.2 ms: 1.42x slower                                                |
| Geometric mean  | (ref)                                                  | 1.30x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 481 ms: 1.19x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 379 ms: 1.19x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.03 sec: 1.15x faster                                               |
| async_tree_none            | 472 ms                                                 | 411 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 639 ms: 1.14x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 1.05 sec: 1.10x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 666 ms: 1.09x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 532 ms: 1.08x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                                |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                                |
| pathlib                    | 19.3 ms                                                | 19.0 ms: 1.02x faster                                                |
| pickle_list                | 5.08 us                                                | 5.03 us: 1.01x faster                                                |
| pickle_dict                | 35.5 us                                                | 36.0 us: 1.01x slower                                                |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                                |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 111 ms: 1.04x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                |
| pickle                     | 11.6 us                                                | 12.1 us: 1.05x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.25 ms: 1.05x slower                                                |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.87 sec: 1.05x slower                                               |
| json                       | 5.26 ms                                                | 5.53 ms: 1.05x slower                                                |
| tornado_http               | 103 ms                                                 | 108 ms: 1.05x slower                                                 |
| dask                       | 372 ms                                                 | 395 ms: 1.06x slower                                                 |
| mypy2                      | 830 ms                                                 | 886 ms: 1.07x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 526 ms: 1.07x slower                                                 |
| logging_simple             | 6.46 us                                                | 6.97 us: 1.08x slower                                                |
| logging_format             | 7.23 us                                                | 7.83 us: 1.08x slower                                                |
| async_generators           | 463 ms                                                 | 504 ms: 1.09x slower                                                 |
| float                      | 84.7 ms                                                | 92.6 ms: 1.09x slower                                                |
| sqlite_synth               | 2.83 us                                                | 3.10 us: 1.09x slower                                                |
| mdp                        | 2.63 sec                                               | 2.91 sec: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                |
| aiohttp                    | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                |
| gunicorn                   | 1.24 ms                                                | 1.41 ms: 1.13x slower                                                |
| dulwich_log                | 68.5 ms                                                | 77.9 ms: 1.14x slower                                                |
| raytrace                   | 312 ms                                                 | 357 ms: 1.14x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 194 ms: 1.15x slower                                                 |
| meteor_contest             | 112 ms                                                 | 129 ms: 1.15x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 71.4 ms: 1.16x slower                                                |
| fannkuch                   | 417 ms                                                 | 483 ms: 1.16x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 104 ms: 1.16x slower                                                 |
| scimark_fft                | 382 ms                                                 | 445 ms: 1.17x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 27.1 ms: 1.17x slower                                                |
| bench_thread_pool          | 842 us                                                 | 991 us: 1.18x slower                                                 |
| mako                       | 11.9 ms                                                | 14.2 ms: 1.19x slower                                                |
| spectral_norm              | 115 ms                                                 | 137 ms: 1.19x slower                                                 |
| tomli_loads                | 2.33 sec                                               | 2.81 sec: 1.21x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 25.9 ms: 1.21x slower                                                |
| chameleon                  | 7.41 ms                                                | 9.02 ms: 1.22x slower                                                |
| crypto_pyaes               | 81.9 ms                                                | 99.9 ms: 1.22x slower                                                |
| sympy_str                  | 300 ms                                                 | 366 ms: 1.22x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.20 ms: 1.23x slower                                                |
| scimark_sor                | 129 ms                                                 | 158 ms: 1.23x slower                                                 |
| comprehensions             | 21.8 us                                                | 27.1 us: 1.24x slower                                                |
| deltablue                  | 3.72 ms                                                | 4.67 ms: 1.26x slower                                                |
| nbody                      | 97.0 ms                                                | 123 ms: 1.27x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.87 ms: 1.27x slower                                                |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                |
| pyflate                    | 482 ms                                                 | 619 ms: 1.28x slower                                                 |
| sympy_expand               | 478 ms                                                 | 614 ms: 1.28x slower                                                 |
| 2to3                       | 274 ms                                                 | 357 ms: 1.30x slower                                                 |
| chaos                      | 67.0 ms                                                | 87.6 ms: 1.31x slower                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 99.5 ms: 1.32x slower                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.81 ms: 1.33x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 2.24 ms: 1.33x slower                                                |
| deepcopy_reduce            | 3.35 us                                                | 4.45 us: 1.33x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.60 sec: 1.36x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 75.4 ms: 1.37x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 217 us: 1.38x slower                                                 |
| deepcopy_memo              | 40.7 us                                                | 56.6 us: 1.39x slower                                                |
| deepcopy                   | 371 us                                                 | 518 us: 1.40x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 154 ms: 1.40x slower                                                 |
| django_template            | 34.6 ms                                                | 49.2 ms: 1.42x slower                                                |
| unpickle_pure_python       | 230 us                                                 | 331 us: 1.44x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 171 ms: 1.45x slower                                                 |
| logging_silent             | 104 ns                                                 | 152 ns: 1.46x slower                                                 |
| regex_compile              | 148 ms                                                 | 220 ms: 1.48x slower                                                 |
| go                         | 139 ms                                                 | 208 ms: 1.49x slower                                                 |
| telco                      | 7.10 ms                                                | 10.7 ms: 1.51x slower                                                |
| richards_super             | 51.5 ms                                                | 79.4 ms: 1.54x slower                                                |
| richards                   | 45.8 ms                                                | 71.0 ms: 1.55x slower                                                |
| pprint_safe_repr           | 776 ms                                                 | 1.21 sec: 1.56x slower                                               |
| pickle_pure_python         | 324 us                                                 | 525 us: 1.62x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.55 sec: 1.62x slower                                               |
| hexiom                     | 6.41 ms                                                | 10.7 ms: 1.66x slower                                                |
| nqueens                    | 83.3 ms                                                | 141 ms: 1.69x slower                                                 |
| generators                 | 31.2 ms                                                | 65.9 ms: 2.11x slower                                                |
| Geometric mean             | (ref)                                                  | 1.18x slower                                                         |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240505-3.13.0a6+-a8158ae-PYTHON_UOPS/bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.98x