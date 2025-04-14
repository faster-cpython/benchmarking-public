# Results vs. 3.12.0

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: linux-x86_64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.82x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 517 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.37x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                  |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| pidigits       | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 123 ms: 1.20x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                  |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                                   |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 208 us: 1.11x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                   |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.3 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.6 ms: 1.13x faster                                                  |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.82x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| deepcopy                   | 371 us                                                 | 243 us: 1.53x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 517 ms: 1.40x faster                                                   |
| spectral_norm              | 115 ms                                                 | 81.9 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.37x faster                                                   |
| scimark_fft                | 382 ms                                                 | 284 ms: 1.35x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.50 us: 1.34x faster                                                  |
| pathlib                    | 19.3 ms                                                | 14.7 ms: 1.31x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                 |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 58.7 ms: 1.28x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 3.99 ms: 1.27x faster                                                  |
| chaos                      | 67.0 ms                                                | 54.3 ms: 1.23x faster                                                  |
| scimark_sor                | 129 ms                                                 | 106 ms: 1.22x faster                                                   |
| logging_format             | 7.23 us                                                | 5.94 us: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                   |
| regex_compile              | 148 ms                                                 | 123 ms: 1.20x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.39 us: 1.20x faster                                                  |
| pyflate                    | 482 ms                                                 | 403 ms: 1.20x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.11 ms: 1.16x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                                  |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                   |
| logging_silent             | 104 ns                                                 | 91.0 ns: 1.15x faster                                                  |
| async_generators           | 463 ms                                                 | 403 ms: 1.15x faster                                                   |
| generators                 | 31.2 ms                                                | 27.3 ms: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                  |
| richards                   | 45.8 ms                                                | 40.2 ms: 1.14x faster                                                  |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                   |
| django_template            | 34.6 ms                                                | 30.6 ms: 1.13x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 105 ms: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.2 ms: 1.12x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 208 us: 1.11x faster                                                   |
| richards_super             | 51.5 ms                                                | 47.1 ms: 1.09x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.55 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                   |
| nqueens                    | 83.3 ms                                                | 77.1 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.63 us: 1.08x faster                                                  |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                 |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                   |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 153 us: 1.03x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.51 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.45 ms: 1.04x slower                                                  |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.88 sec: 1.09x slower                                                 |
| coverage                   | 72.7 ms                                                | 80.8 ms: 1.11x slower                                                  |
| pidigits                   | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 12.3 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.53 ms: 1.71x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 79.5 ms: 3.31x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (3): telco, asyncio_websockets, meteor_contest
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250213-3.14.0a5+-1b27f36-CLANG,JIT/bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x