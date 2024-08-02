# Results vs. 3.12.0

- fork: python
- ref: ac37a806018cc40fafeb
- machine: linux-x86_64
- commit hash: ac37a80
- commit date: 2024-06-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                |
| tornado_http   | 103 ms                                                 | 93.8 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.33x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 930 ms: 1.27x faster                                                  |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 976 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 630 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.3 ms: 1.10x faster                                                 |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.05x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                  |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.49 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                 |
| django_template | 34.6 ms                                                | 34.4 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 266 us: 1.39x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 339 ms: 1.33x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 930 ms: 1.27x faster                                                  |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 466 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 976 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 630 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                 |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| chaos                      | 67.0 ms                                                | 60.9 ms: 1.10x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.3 ms: 1.10x faster                                                 |
| tornado_http               | 103 ms                                                 | 93.8 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                  |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                  |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.57 ms: 1.06x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.05x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.5 ms: 1.05x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 65.5 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                 |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                                  |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                 |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| dask                       | 372 ms                                                 | 367 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                  |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                  |
| django_template            | 34.6 ms                                                | 34.4 ms: 1.01x faster                                                 |
| pickle_list                | 5.08 us                                                | 5.05 us: 1.01x faster                                                 |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.00x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.01x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.02x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                 |
| pyflate                    | 482 ms                                                 | 492 ms: 1.02x slower                                                  |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.03x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.49 us: 1.04x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| scimark_sor                | 129 ms                                                 | 135 ms: 1.04x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.04x slower                                                 |
| go                         | 139 ms                                                 | 146 ms: 1.04x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                |
| richards                   | 45.8 ms                                                | 49.0 ms: 1.07x slower                                                 |
| richards_super             | 51.5 ms                                                | 55.1 ms: 1.07x slower                                                 |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| telco                      | 7.10 ms                                                | 8.40 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.28x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (5): sqlglot_normalize, sqlglot_optimize, xml_etree_parse, scimark_lu, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240617-3.14.0a0-ac37a80/bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x