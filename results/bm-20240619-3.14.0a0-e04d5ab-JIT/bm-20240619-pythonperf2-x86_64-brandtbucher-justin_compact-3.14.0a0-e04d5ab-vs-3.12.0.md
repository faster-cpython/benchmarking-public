# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.00x slower
- HPT reliability: 53.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 307 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 872 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                        |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 913 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 628 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                       |
| float          | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 242 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.7 ms: 1.03x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 32.1 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.53 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.91 us: 1.05x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.47 ms: 1.10x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 40.9 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 36.8 us                                                      | 28.3 us: 1.30x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 872 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                        |
| deepcopy                   | 368 us                                                       | 308 us: 1.20x faster                                                        |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.2 ms: 1.14x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 913 ms: 1.14x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 81.9 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 628 ms: 1.11x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.0 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.08 us: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.98 ms: 1.06x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.38 us: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.4 ms: 1.04x faster                                                       |
| nbody                      | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.7 ms: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| float                      | 76.6 ms                                                      | 74.6 ms: 1.03x faster                                                       |
| fannkuch                   | 350 ms                                                       | 342 ms: 1.02x faster                                                        |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 795 ms: 1.02x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 32.1 us: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                       |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| pyflate                    | 439 ms                                                       | 447 ms: 1.02x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 165 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.53 us: 1.02x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 65.9 ms: 1.03x slower                                                       |
| dask                       | 392 ms                                                       | 404 ms: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.1 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 983 us: 1.03x slower                                                        |
| sympy_str                  | 302 ms                                                       | 314 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.04x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.91 us: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 96.1 ms: 1.07x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.9 ms: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.7 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 307 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.51 ms: 1.08x slower                                                       |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.09x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                       |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.47 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 63.7 ms: 1.11x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.68 ms: 1.12x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.69 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.14x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.06 ms: 1.16x slower                                                       |
| scimark_sor                | 109 ms                                                       | 127 ms: 1.17x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 122 ms: 1.23x slower                                                        |
| coverage                   | 66.7 ms                                                      | 85.2 ms: 1.28x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (8): raytrace, tomli_loads, asyncio_tcp_ssl, xml_etree_process, asyncio_tcp, richards, bench_mp_pool, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 53.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x