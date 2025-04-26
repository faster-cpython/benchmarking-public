# Results vs. 3.12.0

- fork: python
- ref: ce453e6c2ffda657d9d7
- machine: linux-x86_64
- commit hash: ce453e6
- commit date: 2024-11-18
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.8 ms: 1.06x faster                                                  |
| nbody          | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| json_loads           | 28.5 us                                                | 26.8 us: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.0 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                  |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.11x faster                                                  |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.3 ms: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                   |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                   |
| json                       | 5.26 ms                                                | 4.91 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.07x faster                                                  |
| float                      | 84.7 ms                                                | 79.8 ms: 1.06x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                   |
| nbody                      | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                  |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                  |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                   |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                   |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.75 ms: 1.86x slower                                                  |
| dask                       | 372 ms                                                 | 786 ms: 2.11x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.9 ms: 3.33x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (5): xml_etree_parse, pycparser, scimark_sparse_mat_mult, richards, asyncio_websockets
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20241118-3.14.0a1+-ce453e6/bm-20241118-linux-x86_64-python-ce453e6c2ffda657d9d7-3.14.0a1+-ce453e6.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x