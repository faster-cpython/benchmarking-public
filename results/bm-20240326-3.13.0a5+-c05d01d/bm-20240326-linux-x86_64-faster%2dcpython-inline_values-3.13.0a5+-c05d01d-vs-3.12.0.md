# Results vs. 3.12.0

- fork: faster-cpython
- ref: inline_values
- machine: linux-x86_64
- commit hash: c05d01d
- commit date: 2024-03-26
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                      |
| chameleon      | 7.41 ms                                                | 6.88 ms: 1.08x faster                                                     |
| tornado_http   | 103 ms                                                 | 94.2 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.29x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 611 ms: 1.19x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                     |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                     |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                                     |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                     |
| unpickle             | 15.9 us                                                | 16.2 us: 1.02x slower                                                     |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                      |
| pickle_list          | 5.08 us                                                | 5.25 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| python_startup_no_site | 6.94 ms                                                | 8.87 ms: 1.28x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.42x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 440 ms: 1.31x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.29x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                      |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                      |
| raytrace                   | 312 ms                                                 | 257 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 609 ms: 1.19x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 611 ms: 1.19x faster                                                      |
| unpack_sequence            | 54.0 ns                                                | 45.6 ns: 1.18x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 71.0 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                     |
| mypy2                      | 830 ms                                                 | 737 ms: 1.13x faster                                                      |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                                     |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                                      |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.87 us: 1.10x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 37.2 us: 1.09x faster                                                     |
| tornado_http               | 103 ms                                                 | 94.2 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                      |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                      |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                     |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                     |
| scimark_fft                | 382 ms                                                 | 354 ms: 1.08x faster                                                      |
| chameleon                  | 7.41 ms                                                | 6.88 ms: 1.08x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                     |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                      |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                      |
| deepcopy                   | 371 us                                                 | 349 us: 1.06x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 3.17 us: 1.05x faster                                                     |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                                     |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                      |
| pathlib                    | 19.3 ms                                                | 18.6 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                    |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                     |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                     |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                                     |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                      |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 826 us: 1.02x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                      |
| go                         | 139 ms                                                 | 139 ms: 1.01x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                     |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                     |
| unpickle                   | 15.9 us                                                | 16.2 us: 1.02x slower                                                     |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                      |
| aiohttp                    | 1.15 ms                                                | 1.18 ms: 1.02x slower                                                     |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                                     |
| sqlite_synth               | 2.83 us                                                | 2.92 us: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                     |
| pickle_list                | 5.08 us                                                | 5.25 us: 1.03x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 569 ms: 1.03x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.53 ms: 1.03x slower                                                     |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| json                       | 5.26 ms                                                | 5.47 ms: 1.04x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 513 ms: 1.05x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 8.50 ms: 1.20x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.87 ms: 1.28x slower                                                     |
| coverage                   | 72.7 ms                                                | 98.3 ms: 1.35x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (6): dask, richards, mdp, sqlglot_optimize, docutils, richards_super
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: django_template, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240326-3.13.0a5+-c05d01d/bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: 0.95x