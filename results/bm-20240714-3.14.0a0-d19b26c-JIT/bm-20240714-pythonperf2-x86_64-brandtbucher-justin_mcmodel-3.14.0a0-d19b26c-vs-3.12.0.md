# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x faster
- HPT reliability: 89.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 298 ms: 1.05x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.10 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 383 ms: 1.41x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                        |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 801 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 540 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.1 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 73.2 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 262 ms: 1.10x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 8.96 ms: 1.12x faster                                                       |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 383 ms: 1.41x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                        |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 801 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 540 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 811 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.6 us: 1.28x faster                                                       |
| deepcopy                   | 368 us                                                       | 301 us: 1.22x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.1 ms: 1.15x faster                                                       |
| mako                       | 10.0 ms                                                      | 8.96 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.11x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.11x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.4 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.1 ms: 1.08x faster                                                       |
| raytrace                   | 298 ms                                                       | 275 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.27 us: 1.07x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.0 ms: 1.06x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                      |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                       |
| float                      | 76.6 ms                                                      | 73.2 ms: 1.05x faster                                                       |
| async_generators           | 390 ms                                                       | 376 ms: 1.04x faster                                                        |
| richards_super             | 51.3 ms                                                      | 49.6 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.9 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 794 ms: 1.02x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| fannkuch                   | 350 ms                                                       | 346 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| dulwich_log                | 65.4 ms                                                      | 65.9 ms: 1.01x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                        |
| dask                       | 392 ms                                                       | 397 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                      |
| go                         | 150 ms                                                       | 155 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                       |
| 2to3                       | 285 ms                                                       | 298 ms: 1.05x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 94.7 ms: 1.05x slower                                                       |
| sympy_expand               | 484 ms                                                       | 512 ms: 1.06x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 25.4 ms: 1.06x slower                                                       |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                       |
| json                       | 5.12 ms                                                      | 5.50 ms: 1.07x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.10 sec: 1.08x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 62.2 ms: 1.08x slower                                                       |
| regex_dna                  | 239 ms                                                       | 262 ms: 1.10x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.57 ms: 1.10x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.57 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 105 ns: 1.11x slower                                                        |
| scimark_sor                | 109 ms                                                       | 124 ms: 1.14x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.35 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.8 ms: 1.24x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 123 ms: 1.24x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.43 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (9): xml_etree_parse, scimark_sparse_mat_mult, pyflate, tornado_http, sympy_str, regex_effbot, asyncio_tcp, bench_mp_pool, chaos
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 89.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x