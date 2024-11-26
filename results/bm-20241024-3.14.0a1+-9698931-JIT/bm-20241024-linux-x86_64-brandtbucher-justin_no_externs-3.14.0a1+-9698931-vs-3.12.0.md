# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.034x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 301 ms: 1.10x slower                                                      |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                    |
| tornado_http   | 103 ms                                                 | 96.7 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 331 ms: 1.36x faster                                                      |
| async_tree_none            | 472 ms                                                 | 352 ms: 1.34x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 433 ms: 1.33x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 880 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 565 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 589 ms: 1.23x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 83.5 ms: 1.01x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| nbody          | 97.0 ms                                                | 102 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 213 ms: 1.01x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                     |
| regex_compile  | 148 ms                                                 | 154 ms: 1.04x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                    |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 152 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 90.4 ms: 1.01x slower                                                     |
| xml_etree_process    | 61.7 ms                                                | 63.7 ms: 1.03x slower                                                     |
| pickle_pure_python   | 324 us                                                 | 349 us: 1.08x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 248 us: 1.08x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                     |
| django_template | 34.6 ms                                                | 39.2 ms: 1.13x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 331 ms: 1.36x faster                                                      |
| async_tree_none            | 472 ms                                                 | 352 ms: 1.34x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 433 ms: 1.33x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 880 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 565 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 589 ms: 1.23x faster                                                      |
| deepcopy                   | 371 us                                                 | 309 us: 1.20x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 35.3 us: 1.15x faster                                                     |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 3.07 us: 1.09x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                    |
| tornado_http               | 103 ms                                                 | 96.7 ms: 1.06x faster                                                     |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 152 ms: 1.05x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.1 ms: 1.03x faster                                                     |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| float                      | 84.7 ms                                                | 83.5 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                      |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.01x slower                                                      |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                     |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                     |
| comprehensions             | 21.8 us                                                | 22.0 us: 1.01x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                     |
| xml_etree_generate         | 89.2 ms                                                | 90.4 ms: 1.01x slower                                                     |
| mako                       | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 151 ms: 1.03x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 63.7 ms: 1.03x slower                                                     |
| crypto_pyaes               | 81.9 ms                                                | 84.6 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.23 ms: 1.04x slower                                                     |
| regex_compile              | 148 ms                                                 | 154 ms: 1.04x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                      |
| raytrace                   | 312 ms                                                 | 327 ms: 1.05x slower                                                      |
| nbody                      | 97.0 ms                                                | 102 ms: 1.06x slower                                                      |
| deltablue                  | 3.72 ms                                                | 3.93 ms: 1.06x slower                                                     |
| sympy_str                  | 300 ms                                                 | 321 ms: 1.07x slower                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 80.7 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.47 ms: 1.08x slower                                                     |
| pickle_pure_python         | 324 us                                                 | 349 us: 1.08x slower                                                      |
| unpickle_pure_python       | 230 us                                                 | 248 us: 1.08x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                                    |
| meteor_contest             | 112 ms                                                 | 122 ms: 1.09x slower                                                      |
| chaos                      | 67.0 ms                                                | 72.9 ms: 1.09x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 184 ms: 1.09x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.29 sec: 1.09x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 921 us: 1.09x slower                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.84 ms: 1.09x slower                                                     |
| 2to3                       | 274 ms                                                 | 301 ms: 1.10x slower                                                      |
| sympy_expand               | 478 ms                                                 | 525 ms: 1.10x slower                                                      |
| pyflate                    | 482 ms                                                 | 531 ms: 1.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                     |
| pprint_safe_repr           | 776 ms                                                 | 870 ms: 1.12x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 125 ms: 1.13x slower                                                      |
| django_template            | 34.6 ms                                                | 39.2 ms: 1.13x slower                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.81 sec: 1.15x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 183 us: 1.16x slower                                                      |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                     |
| fannkuch                   | 417 ms                                                 | 486 ms: 1.16x slower                                                      |
| scimark_sor                | 129 ms                                                 | 151 ms: 1.17x slower                                                      |
| logging_silent             | 104 ns                                                 | 122 ns: 1.17x slower                                                      |
| spectral_norm              | 115 ms                                                 | 135 ms: 1.17x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 25.2 ms: 1.18x slower                                                     |
| go                         | 139 ms                                                 | 165 ms: 1.18x slower                                                      |
| telco                      | 7.10 ms                                                | 8.42 ms: 1.19x slower                                                     |
| richards_super             | 51.5 ms                                                | 61.5 ms: 1.19x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 65.7 ms: 1.20x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.70 ms: 1.24x slower                                                     |
| nqueens                    | 83.3 ms                                                | 107 ms: 1.28x slower                                                      |
| richards                   | 45.8 ms                                                | 59.1 ms: 1.29x slower                                                     |
| generators                 | 31.2 ms                                                | 41.6 ms: 1.33x slower                                                     |
| hexiom                     | 6.41 ms                                                | 8.79 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (2): scimark_fft, async_generators
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.14x