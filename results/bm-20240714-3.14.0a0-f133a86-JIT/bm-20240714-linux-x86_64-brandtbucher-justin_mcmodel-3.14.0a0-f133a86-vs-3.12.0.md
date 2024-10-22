# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: f133a86
- commit date: 2024-07-14
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                |
| tornado_http   | 103 ms                                                 | 93.2 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                  |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 77.1 ms: 1.26x faster                                                 |
| float          | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                 |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| pickle_pure_python   | 324 us                                                 | 294 us: 1.10x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.9 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                 |
| django_template | 34.6 ms                                                | 35.1 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                  |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 847 ms: 1.40x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                  |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                  |
| nbody                      | 97.0 ms                                                | 77.1 ms: 1.26x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.3 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| float                      | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                 |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                                 |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                                  |
| chaos                      | 67.0 ms                                                | 57.4 ms: 1.17x faster                                                 |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| fannkuch                   | 417 ms                                                 | 365 ms: 1.14x faster                                                  |
| richards                   | 45.8 ms                                                | 40.8 ms: 1.12x faster                                                 |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 294 us: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.2 ms: 1.10x faster                                                 |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                 |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 99.9 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                                 |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                  |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                 |
| 2to3                       | 274 ms                                                 | 269 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                 |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 54.6 ms: 1.00x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.47 ms: 1.01x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 21.7 ms: 1.01x slower                                                 |
| django_template            | 34.6 ms                                                | 35.1 ms: 1.02x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                 |
| sympy_expand               | 478 ms                                                 | 492 ms: 1.03x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.8 ms: 1.03x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.09 ms: 1.14x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                 |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): bench_mp_pool, async_generators, scimark_sor, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240714-3.14.0a0-f133a86-JIT/bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x