# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.016x slower
- HPT reliability: 93.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 297 ms: 1.04x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 376 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                       |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 416 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 857 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 584 ms: 1.19x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                       |
| float          | 76.6 ms                                                      | 80.1 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                      |
| regex_dna      | 239 ms                                                       | 249 ms: 1.05x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                       | 197 us: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 83.1 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                     |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 152 ms: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                      |
| python_startup         | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.49 ms: 1.05x faster                                                      |
| django_template | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 376 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                       |
| async_tree_none            | 452 ms                                                       | 340 ms: 1.33x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 416 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 563 ms: 1.24x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 30.2 us: 1.22x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 857 ms: 1.22x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 584 ms: 1.19x faster                                                       |
| deepcopy                   | 368 us                                                       | 318 us: 1.16x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.15x faster                                                      |
| comprehensions             | 21.9 us                                                      | 19.9 us: 1.10x faster                                                      |
| crypto_pyaes               | 80.3 ms                                                      | 73.6 ms: 1.09x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                      |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.13 us: 1.08x faster                                                      |
| unpickle_pure_python       | 210 us                                                       | 197 us: 1.06x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.2 ms: 1.06x faster                                                      |
| richards_super             | 51.3 ms                                                      | 48.7 ms: 1.05x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.49 ms: 1.05x faster                                                      |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 83.1 ms: 1.04x faster                                                      |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                      |
| scimark_lu                 | 98.8 ms                                                      | 97.0 ms: 1.02x faster                                                      |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                     |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.01x faster                                                     |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                      |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                     |
| sympy_sum                  | 162 ms                                                       | 163 ms: 1.01x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 95.1 ns: 1.01x slower                                                      |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 817 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.28 ms: 1.01x slower                                                      |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                      |
| go                         | 150 ms                                                       | 153 ms: 1.02x slower                                                       |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 68.0 ms: 1.04x slower                                                      |
| 2to3                       | 285 ms                                                       | 297 ms: 1.04x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                      |
| chaos                      | 64.0 ms                                                      | 66.7 ms: 1.04x slower                                                      |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.05x slower                                                       |
| float                      | 76.6 ms                                                      | 80.1 ms: 1.05x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 152 ms: 1.05x slower                                                       |
| sympy_str                  | 302 ms                                                       | 319 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 463 ms: 1.06x slower                                                       |
| generators                 | 37.4 ms                                                      | 39.9 ms: 1.07x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 98.5 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.92 ms: 1.08x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.09x slower                                                      |
| telco                      | 6.96 ms                                                      | 7.62 ms: 1.09x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                     |
| raytrace                   | 298 ms                                                       | 327 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 64.0 ms: 1.11x slower                                                      |
| django_template            | 38.2 ms                                                      | 42.7 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.12x slower                                                       |
| sympy_expand               | 484 ms                                                       | 545 ms: 1.13x slower                                                       |
| fannkuch                   | 350 ms                                                       | 394 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.78 ms: 1.14x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 80.4 ms: 1.21x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 7.27 ms: 1.22x slower                                                      |
| async_generators           | 390 ms                                                       | 482 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 6.10 ms: 1.75x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                      |
| bench_mp_pool              | 4.76 ms                                                      | 1.60 sec: 335.51x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                               |

Benchmark hidden because not significant (5): nbody, sqlalchemy_imperative, scimark_monte_carlo, pycparser, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.016x slower
# HPT report

- Reliability score: 93.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x