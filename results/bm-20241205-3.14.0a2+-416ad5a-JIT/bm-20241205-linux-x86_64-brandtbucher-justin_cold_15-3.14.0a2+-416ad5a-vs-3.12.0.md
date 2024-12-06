# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_15
- machine: linux-x86_64
- commit hash: 416ad5a
- commit date: 2024-12-05
- overall geometric mean: 1.106x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                  |
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 197 us: 1.17x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.9 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                  |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                  |
| deepcopy                   | 371 us                                                 | 272 us: 1.36x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                  |
| richards                   | 45.8 ms                                                | 37.5 ms: 1.22x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                 |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                  |
| richards_super             | 51.5 ms                                                | 43.4 ms: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 197 us: 1.17x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 130 ms: 1.15x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                  |
| logging_format             | 7.23 us                                                | 6.41 us: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.9 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.86 us: 1.10x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                   |
| json                       | 5.26 ms                                                | 4.82 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                 |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                  |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                   |
| telco                      | 7.10 ms                                                | 7.53 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| nqueens                    | 83.3 ms                                                | 90.4 ms: 1.09x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.3 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (4): spectral_norm, logging_silent, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241205-3.14.0a2+-416ad5a-JIT/bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x