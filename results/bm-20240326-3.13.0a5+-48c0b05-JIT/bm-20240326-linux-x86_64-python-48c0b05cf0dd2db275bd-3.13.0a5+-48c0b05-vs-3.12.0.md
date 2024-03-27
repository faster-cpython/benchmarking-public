# Results vs. 3.12.0

- fork: python
- ref: 48c0b05cf0dd2db275bd
- machine: linux-x86_64
- commit hash: 48c0b05
- commit date: 2024-03-26
- overall geometric mean: 1.02x faster
- HPT reliability: 73.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                   |
| chameleon      | 7.41 ms                                                | 6.88 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                 |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 354 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 615 ms: 1.18x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| regex_dna      | 212 ms                                                 | 217 ms: 1.03x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                   |
| unpickle             | 15.9 us                                                | 15.2 us: 1.05x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 241 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): unpickle_list, pickle, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.0 ms: 1.16x slower                                                  |
| python_startup_no_site | 6.94 ms                                                | 9.48 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                  |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.42x faster                                                   |
| async_tree_none            | 472 ms                                                 | 354 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 450 ms: 1.28x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 602 ms: 1.20x faster                                                   |
| comprehensions             | 21.8 us                                                | 18.4 us: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 615 ms: 1.18x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| float                      | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                  |
| logging_format             | 7.23 us                                                | 6.57 us: 1.10x faster                                                  |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.0 ms: 1.09x faster                                                  |
| scimark_fft                | 382 ms                                                 | 351 ms: 1.09x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.96 us: 1.08x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                                  |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                   |
| chameleon                  | 7.41 ms                                                | 6.88 ms: 1.08x faster                                                  |
| chaos                      | 67.0 ms                                                | 63.1 ms: 1.06x faster                                                  |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                                  |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 71.0 ms: 1.06x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.17 us: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                   |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.05x faster                                                  |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.3 us: 1.04x faster                                                  |
| deepcopy                   | 371 us                                                 | 360 us: 1.03x faster                                                   |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 39.5 us: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| pickle_list                | 5.08 us                                                | 4.94 us: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.69 ms: 1.03x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.03x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                  |
| pathlib                    | 19.3 ms                                                | 19.0 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                   |
| regex_compile              | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                   |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                                   |
| dask                       | 372 ms                                                 | 377 ms: 1.01x slower                                                   |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 21.8 ms: 1.02x slower                                                  |
| richards                   | 45.8 ms                                                | 46.7 ms: 1.02x slower                                                  |
| richards_super             | 51.5 ms                                                | 52.6 ms: 1.02x slower                                                  |
| pyflate                    | 482 ms                                                 | 493 ms: 1.02x slower                                                   |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                   |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.03x slower                                                   |
| sympy_expand               | 478 ms                                                 | 491 ms: 1.03x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 569 ms: 1.03x slower                                                   |
| dulwich_log                | 68.5 ms                                                | 70.9 ms: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 241 us: 1.05x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                 |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                  |
| gunicorn                   | 1.24 ms                                                | 1.31 ms: 1.06x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                                  |
| nqueens                    | 83.3 ms                                                | 90.1 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                  |
| go                         | 139 ms                                                 | 155 ms: 1.11x slower                                                   |
| hexiom                     | 6.41 ms                                                | 7.23 ms: 1.13x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.67 ms: 1.13x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.13x slower                                                   |
| python_startup             | 9.55 ms                                                | 11.0 ms: 1.16x slower                                                  |
| telco                      | 7.10 ms                                                | 8.69 ms: 1.22x slower                                                  |
| coverage                   | 72.7 ms                                                | 96.4 ms: 1.33x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.48 ms: 1.37x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 86.5 ns: 1.60x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (10): mypy2, coroutines, scimark_sparse_mat_mult, pycparser, bench_mp_pool, async_generators, unpickle_list, pickle, json_loads, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240326-3.13.0a5+-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 73.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.03x