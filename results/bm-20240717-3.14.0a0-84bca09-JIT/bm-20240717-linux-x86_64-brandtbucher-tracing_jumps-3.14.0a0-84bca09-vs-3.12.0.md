# Results vs. 3.12.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 84bca09
- commit date: 2024-07-17
- overall geometric mean: 1.08x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                 |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                               |
| tornado_http   | 103 ms                                                 | 93.2 ms: 1.10x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 846 ms: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                |
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                |
| pickle_pure_python   | 324 us                                                 | 293 us: 1.11x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                 |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 846 ms: 1.37x faster                                                 |
| deepcopy                   | 371 us                                                 | 276 us: 1.35x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.35x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.9 ms: 1.23x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                |
| nbody                      | 97.0 ms                                                | 79.5 ms: 1.22x faster                                                |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.16x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.35 ms: 1.16x faster                                                |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                                 |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                 |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                                 |
| richards                   | 45.8 ms                                                | 41.3 ms: 1.11x faster                                                |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 293 us: 1.11x faster                                                 |
| tornado_http               | 103 ms                                                 | 93.2 ms: 1.10x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 450 ms: 1.03x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                |
| bench_thread_pool          | 842 us                                                 | 828 us: 1.02x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                                |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.6 ms: 1.03x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.03x slower                                                 |
| sympy_expand               | 478 ms                                                 | 496 ms: 1.04x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                               |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.68 ms: 1.04x slower                                                |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                |
| coverage                   | 72.7 ms                                                | 93.6 ms: 1.29x slower                                                |
| generators                 | 31.2 ms                                                | 45.4 ms: 1.45x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): coroutines, scimark_sor, bench_mp_pool, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240717-3.14.0a0-84bca09-JIT/bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x