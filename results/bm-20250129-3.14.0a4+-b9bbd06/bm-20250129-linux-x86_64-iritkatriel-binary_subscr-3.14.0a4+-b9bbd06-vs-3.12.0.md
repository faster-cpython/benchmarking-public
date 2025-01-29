# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: b9bbd06
- commit date: 2025-01-29
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                 |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                 |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.78x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| nbody          | 97.0 ms                                                | 99.6 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.13 ms: 1.15x faster                                                |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                 |
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 97.0 ms: 1.10x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                 |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.78x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                 |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                |
| async_generators           | 463 ms                                                 | 385 ms: 1.20x faster                                                 |
| float                      | 84.7 ms                                                | 71.6 ms: 1.18x faster                                                |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.16x faster                                                |
| spectral_norm              | 115 ms                                                 | 98.7 ms: 1.16x faster                                                |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.13 ms: 1.15x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                |
| scimark_fft                | 382 ms                                                 | 346 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 97.0 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.69 ms: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                               |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 76.9 ms: 1.06x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                 |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 52.7 ms: 1.04x faster                                                |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                               |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                                |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                                |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                 |
| fannkuch                   | 417 ms                                                 | 421 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                |
| bench_thread_pool          | 842 us                                                 | 864 us: 1.03x slower                                                 |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                 |
| nbody                      | 97.0 ms                                                | 99.6 ms: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                |
| coverage                   | 72.7 ms                                                | 89.9 ms: 1.24x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (3): scimark_lu, regex_dna, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-b9bbd06/bm-20250129-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-b9bbd06.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x