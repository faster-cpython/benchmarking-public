# Results vs. 3.12.0

- fork: python
- ref: 117a8acdab997b73ada8
- machine: linux-x86_64
- commit hash: 117a8ac
- commit date: 2024-06-02
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| tornado_http   | 103 ms                                                 | 91.8 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 329 ms: 1.36x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 428 ms: 1.34x faster                                                  |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.28x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 462 ms: 1.25x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 592 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 973 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 601 ms: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| nbody          | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                 |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 14.2 ms: 1.49x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 329 ms: 1.36x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 428 ms: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                 |
| async_tree_none            | 472 ms                                                 | 370 ms: 1.28x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 462 ms: 1.25x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 592 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 973 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 601 ms: 1.21x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 73.2 ms: 1.12x faster                                                 |
| tornado_http               | 103 ms                                                 | 91.8 ms: 1.12x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                  |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                 |
| nbody                      | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.10x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                 |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.07 ms: 1.06x faster                                                 |
| async_generators           | 463 ms                                                 | 439 ms: 1.06x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                  |
| deepcopy                   | 371 us                                                 | 353 us: 1.05x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 65.4 ms: 1.05x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                                 |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 3.22 us: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.9 ms: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 824 us: 1.02x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.72 sec: 1.02x faster                                                |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                 |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                 |
| richards                   | 45.8 ms                                                | 50.5 ms: 1.10x slower                                                 |
| richards_super             | 51.5 ms                                                | 57.2 ms: 1.11x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.28 ms: 1.13x slower                                                 |
| telco                      | 7.10 ms                                                | 8.42 ms: 1.19x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                 |
| python_startup             | 9.55 ms                                                | 14.2 ms: 1.49x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): logging_silent, bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (26) of results/bm-20240602-3.14.0a0-117a8ac/bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x