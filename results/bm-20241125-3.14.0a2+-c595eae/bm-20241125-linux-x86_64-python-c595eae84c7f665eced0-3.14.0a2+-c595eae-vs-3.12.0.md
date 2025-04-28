# Results vs. 3.12.0

- fork: python
- ref: c595eae84c7f665eced0
- machine: linux-x86_64
- commit hash: c595eae
- commit date: 2024-11-25
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                   |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 340 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 928 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 82.5 ms: 1.03x faster                                                  |
| nbody          | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                 |
| json_loads           | 28.5 us                                                | 26.0 us: 1.10x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 329 us: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                  |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                   |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                   |
| deepcopy                   | 371 us                                                 | 264 us: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 340 ms: 1.32x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 928 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 571 ms: 1.27x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                  |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                  |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| generators                 | 31.2 ms                                                | 27.3 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.10x faster                                                  |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                                  |
| json                       | 5.26 ms                                                | 4.84 ms: 1.09x faster                                                  |
| async_generators           | 463 ms                                                 | 431 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 70.1 ms: 1.07x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.1 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.05x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.91 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| float                      | 84.7 ms                                                | 82.5 ms: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                   |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                   |
| scimark_fft                | 382 ms                                                 | 376 ms: 1.02x faster                                                   |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| nbody                      | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.43 ms: 1.00x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                   |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 329 us: 1.01x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                  |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.72 ms: 1.84x slower                                                  |
| dask                       | 372 ms                                                 | 780 ms: 2.10x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (4): asyncio_websockets, pycparser, sqlite_synth, spectral_norm
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20241125-3.14.0a2+-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x