# Results vs. 3.12.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 325408b
- commit date: 2025-04-03
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| regex_dna      | 212 ms                                                 | 203 ms: 1.05x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.01x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                               |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                |
| json_loads           | 28.5 us                                                | 29.5 us: 1.03x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.16 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                               |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                               |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                               |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                |
| spectral_norm              | 115 ms                                                 | 96.3 ms: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                               |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                               |
| dulwich_log                | 68.5 ms                                                | 58.3 ms: 1.18x faster                                               |
| async_generators           | 463 ms                                                 | 394 ms: 1.18x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                               |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                               |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                               |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.11x faster                                               |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                               |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                               |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                               |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.06x faster                                               |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                              |
| logging_silent             | 104 ns                                                 | 98.9 ns: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                              |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.05x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                               |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                               |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                               |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                               |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                                |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| fannkuch                   | 417 ms                                                 | 429 ms: 1.03x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                               |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.04x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                               |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                               |
| coverage                   | 72.7 ms                                                | 83.2 ms: 1.14x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.16 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, nbody, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-325408b/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x