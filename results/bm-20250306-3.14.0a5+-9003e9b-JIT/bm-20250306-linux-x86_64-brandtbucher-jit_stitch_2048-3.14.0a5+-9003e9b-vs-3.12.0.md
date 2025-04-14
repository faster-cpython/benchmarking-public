# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_stitch_2048
- machine: linux-x86_64
- commit hash: 9003e9b
- commit date: 2025-03-06
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                    |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                   |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                    |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                   |
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                    |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                                   |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                    |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                   |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                    |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                    |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                   |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                    |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                    |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.50 ms: 1.12x faster                                                   |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                   |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                   |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                    |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                    |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                    |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                  |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                    |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.04x faster                                                   |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                   |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                    |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.08x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.56 ms: 1.20x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.43 ms: 1.64x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (5): pycparser, scimark_lu, pickle_pure_python, asyncio_websockets, logging_silent
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-9003e9b-JIT/bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x