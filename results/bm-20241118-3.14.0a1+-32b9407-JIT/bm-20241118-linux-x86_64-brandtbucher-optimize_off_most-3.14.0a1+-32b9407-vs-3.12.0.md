# Results vs. 3.12.0

- fork: brandtbucher
- ref: optimize_off_most
- machine: linux-x86_64
- commit hash: 32b9407
- commit date: 2024-11-18
- overall geometric mean: 1.007x slower
- HPT reliability: 88.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 300 ms: 1.09x slower                                                      |
| docutils       | 2.77 sec                                               | 3.27 sec: 1.18x slower                                                    |
| Geometric mean | (ref)                                                  | 1.14x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 342 ms: 1.38x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 328 ms: 1.37x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 573 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 590 ms: 1.23x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.7 ms: 1.05x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| nbody          | 97.0 ms                                                | 98.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 156 ms: 1.05x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                     |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                    |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 60.8 ms: 1.01x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 228 us: 1.01x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 342 us: 1.06x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                     |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                      |
| async_tree_none            | 472 ms                                                 | 342 ms: 1.38x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 328 ms: 1.37x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 573 ms: 1.27x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 32.3 us: 1.26x faster                                                     |
| deepcopy                   | 371 us                                                 | 298 us: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 590 ms: 1.23x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 985 ms: 1.20x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.92 us: 1.14x faster                                                     |
| comprehensions             | 21.8 us                                                | 19.4 us: 1.12x faster                                                     |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                                     |
| scimark_fft                | 382 ms                                                 | 349 ms: 1.09x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| json                       | 5.26 ms                                                | 4.90 ms: 1.07x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                     |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                     |
| float                      | 84.7 ms                                                | 80.7 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 72.9 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.2 ms: 1.03x faster                                                     |
| raytrace                   | 312 ms                                                 | 304 ms: 1.03x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 60.8 ms: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 228 us: 1.01x faster                                                      |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.73 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                      |
| nbody                      | 97.0 ms                                                | 98.9 ms: 1.02x slower                                                     |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 70.8 ms: 1.03x slower                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 152 ms: 1.03x slower                                                      |
| pyflate                    | 482 ms                                                 | 505 ms: 1.05x slower                                                      |
| fannkuch                   | 417 ms                                                 | 437 ms: 1.05x slower                                                      |
| regex_compile              | 148 ms                                                 | 156 ms: 1.05x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                     |
| pickle_pure_python         | 324 us                                                 | 342 us: 1.06x slower                                                      |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                      |
| richards                   | 45.8 ms                                                | 48.8 ms: 1.07x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.80 sec: 1.07x slower                                                    |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                      |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                     |
| sympy_str                  | 300 ms                                                 | 323 ms: 1.08x slower                                                      |
| logging_silent             | 104 ns                                                 | 112 ns: 1.08x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.47 ms: 1.08x slower                                                     |
| go                         | 139 ms                                                 | 151 ms: 1.08x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 915 us: 1.09x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.28 sec: 1.09x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                     |
| 2to3                       | 274 ms                                                 | 300 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 122 ms: 1.10x slower                                                      |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.11x slower                                                      |
| sympy_expand               | 478 ms                                                 | 530 ms: 1.11x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 188 ms: 1.11x slower                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.89 ms: 1.12x slower                                                     |
| richards_super             | 51.5 ms                                                | 57.7 ms: 1.12x slower                                                     |
| nqueens                    | 83.3 ms                                                | 94.2 ms: 1.13x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.36 ms: 1.15x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 25.1 ms: 1.17x slower                                                     |
| pprint_safe_repr           | 776 ms                                                 | 910 ms: 1.17x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 64.7 ms: 1.18x slower                                                     |
| docutils                   | 2.77 sec                                               | 3.27 sec: 1.18x slower                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.89 sec: 1.21x slower                                                    |
| hexiom                     | 6.41 ms                                                | 8.25 ms: 1.29x slower                                                     |
| generators                 | 31.2 ms                                                | 41.0 ms: 1.31x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.81x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 86.6 ms: 3.61x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): chaos, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241118-3.14.0a1+-32b9407-JIT/bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 88.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.16x