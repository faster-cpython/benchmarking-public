# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-x86_64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 587 ms: 1.97x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                  |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| nbody          | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                 |
| pidigits       | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 123 ms: 1.20x faster                                                  |
| regex_dna      | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| unpickle             | 15.9 us                                                | 14.1 us: 1.13x faster                                                 |
| unpickle_list        | 5.29 us                                                | 4.71 us: 1.12x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 88.0 ms: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                 |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                 |
| pickle               | 11.6 us                                                | 13.3 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| mako            | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                                |
| async_tree_io              | 1.16 sec                                               | 587 ms: 1.97x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                  |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                  |
| deepcopy                   | 371 us                                                 | 245 us: 1.51x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                 |
| go                         | 139 ms                                                 | 106 ms: 1.32x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.55 us: 1.31x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.2 ms: 1.27x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 59.2 ms: 1.27x faster                                                 |
| deltablue                  | 3.72 ms                                                | 2.95 ms: 1.26x faster                                                 |
| float                      | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| chaos                      | 67.0 ms                                                | 53.6 ms: 1.25x faster                                                 |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| raytrace                   | 312 ms                                                 | 254 ms: 1.23x faster                                                  |
| spectral_norm              | 115 ms                                                 | 94.4 ms: 1.22x faster                                                 |
| scimark_sor                | 129 ms                                                 | 107 ms: 1.20x faster                                                  |
| regex_compile              | 148 ms                                                 | 123 ms: 1.20x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 57.9 ms: 1.18x faster                                                 |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 144 ms: 1.17x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.3 ms: 1.17x faster                                                 |
| sympy_str                  | 300 ms                                                 | 260 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.38 ms: 1.15x faster                                                 |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                  |
| nbody                      | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                 |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.13x faster                                                 |
| hexiom                     | 6.41 ms                                                | 5.67 ms: 1.13x faster                                                 |
| unpickle                   | 15.9 us                                                | 14.1 us: 1.13x faster                                                 |
| unpickle_list              | 5.29 us                                                | 4.71 us: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                 |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 108 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.96 us: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| sympy_expand               | 478 ms                                                 | 443 ms: 1.08x faster                                                  |
| logging_format             | 7.23 us                                                | 6.72 us: 1.08x faster                                                 |
| regex_dna                  | 212 ms                                                 | 198 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                |
| unpack_sequence            | 54.0 ns                                                | 51.2 ns: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.2 ms: 1.05x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 756 ms: 1.03x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.02x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 88.0 ms: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                 |
| meteor_contest             | 112 ms                                                 | 113 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                                  |
| mako                       | 11.9 ms                                                | 12.1 ms: 1.02x slower                                                 |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                 |
| telco                      | 7.10 ms                                                | 7.30 ms: 1.03x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.30 us: 1.04x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                                 |
| pidigits                   | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                 |
| pickle                     | 11.6 us                                                | 13.3 us: 1.14x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                 |
| dask                       | 372 ms                                                 | 886 ms: 2.38x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 92.7 ms: 3.86x slower                                                 |
| logging_silent             | 104 ns                                                 | 503 ns: 4.82x slower                                                  |
| coverage                   | 72.7 ms                                                | 399 ms: 5.49x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (4): pycparser, asyncio_websockets, asyncio_tcp_ssl, xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (24) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.14x