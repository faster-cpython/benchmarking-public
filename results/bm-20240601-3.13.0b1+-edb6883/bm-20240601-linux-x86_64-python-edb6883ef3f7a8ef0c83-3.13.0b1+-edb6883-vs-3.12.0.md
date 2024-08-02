# Results vs. 3.12.0

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                   |
| chameleon      | 7.41 ms                                                | 6.89 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                 |
| tornado_http   | 103 ms                                                 | 93.8 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                   |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 944 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 608 ms: 1.19x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                  |
| nbody          | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                  |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.17 sec: 1.07x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.21 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 10.8 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 443 ms: 1.30x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                  |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 944 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 608 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                   |
| logging_format             | 7.23 us                                                | 6.38 us: 1.13x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                  |
| mypy2                      | 830 ms                                                 | 734 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                  |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.11x faster                                                  |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.8 ms: 1.09x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.08x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                                  |
| float                      | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                  |
| chameleon                  | 7.41 ms                                                | 6.89 ms: 1.08x faster                                                  |
| nbody                      | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.17 sec: 1.07x faster                                                 |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                  |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 38.3 us: 1.06x faster                                                  |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                  |
| async_generators           | 463 ms                                                 | 440 ms: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.5 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                  |
| deepcopy                   | 371 us                                                 | 358 us: 1.04x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.4 ms: 1.03x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                  |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| scimark_fft                | 382 ms                                                 | 375 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.21 us: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                   |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.1 ms: 1.00x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                  |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                  |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                   |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                 |
| aiohttp                    | 1.15 ms                                                | 1.18 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.19 ms: 1.03x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                   |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 3.01 us: 1.06x slower                                                  |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| richards                   | 45.8 ms                                                | 50.7 ms: 1.11x slower                                                  |
| richards_super             | 51.5 ms                                                | 57.2 ms: 1.11x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| telco                      | 7.10 ms                                                | 8.62 ms: 1.21x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                  |
| coverage                   | 72.7 ms                                                | 92.6 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): dask, django_template, pickle_list, sqlglot_normalize, json, xml_etree_parse
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.98x