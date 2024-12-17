# Results vs. 3.12.0

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.221x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 353 ms: 1.29x slower                                                       |
| docutils       | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.19x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.28 sec: 1.08x slower                                                     |
| async_tree_io              | 1.16 sec                                               | 1.37 sec: 1.18x slower                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 951 ms: 1.31x slower                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 805 ms: 1.40x slower                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.03 sec: 1.42x slower                                                     |
| async_tree_none_tg         | 450 ms                                                 | 679 ms: 1.51x slower                                                       |
| async_tree_memoization     | 578 ms                                                 | 884 ms: 1.53x slower                                                       |
| async_tree_none            | 472 ms                                                 | 733 ms: 1.55x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.36x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                       |
| nbody          | 97.0 ms                                                | 139 ms: 1.43x slower                                                       |
| float          | 84.7 ms                                                | 131 ms: 1.54x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                      |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                       |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                      |
| regex_compile  | 148 ms                                                 | 171 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.9 ms: 1.11x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                                      |
| xml_etree_generate   | 89.2 ms                                                | 97.0 ms: 1.09x slower                                                      |
| tomli_loads          | 2.33 sec                                               | 2.78 sec: 1.19x slower                                                     |
| xml_etree_process    | 61.7 ms                                                | 75.4 ms: 1.22x slower                                                      |
| json_dumps           | 10.4 ms                                                | 13.7 ms: 1.32x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 320 us: 1.39x slower                                                       |
| pickle_pure_python   | 324 us                                                 | 475 us: 1.46x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.76 ms: 1.41x slower                                                      |
| python_startup         | 9.55 ms                                                | 16.3 ms: 1.70x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.55x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 47.3 ms: 1.37x slower                                                      |
| mako            | 11.9 ms                                                | 18.4 ms: 1.54x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.45x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 317 us: 1.17x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 95.9 ms: 1.11x faster                                                      |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.37 us: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.46 ms: 1.04x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.94 us: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.28 sec: 1.08x slower                                                     |
| xml_etree_generate         | 89.2 ms                                                | 97.0 ms: 1.09x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                     |
| async_generators           | 463 ms                                                 | 505 ms: 1.09x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                      |
| crypto_pyaes               | 81.9 ms                                                | 92.5 ms: 1.13x slower                                                      |
| coroutines                 | 23.2 ms                                                | 26.5 ms: 1.15x slower                                                      |
| generators                 | 31.2 ms                                                | 35.9 ms: 1.15x slower                                                      |
| regex_compile              | 148 ms                                                 | 171 ms: 1.15x slower                                                       |
| meteor_contest             | 112 ms                                                 | 131 ms: 1.17x slower                                                       |
| mdp                        | 2.63 sec                                               | 3.07 sec: 1.17x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 80.4 ms: 1.17x slower                                                      |
| scimark_fft                | 382 ms                                                 | 449 ms: 1.18x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 1.37 sec: 1.18x slower                                                     |
| comprehensions             | 21.8 us                                                | 25.8 us: 1.18x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 131 ms: 1.19x slower                                                       |
| nqueens                    | 83.3 ms                                                | 99.1 ms: 1.19x slower                                                      |
| tomli_loads                | 2.33 sec                                               | 2.78 sec: 1.19x slower                                                     |
| spectral_norm              | 115 ms                                                 | 138 ms: 1.20x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 66.1 ms: 1.21x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 26.0 ms: 1.21x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 75.4 ms: 1.22x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.45 sec: 1.23x slower                                                     |
| sympy_str                  | 300 ms                                                 | 373 ms: 1.25x slower                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.34 ms: 1.25x slower                                                      |
| fannkuch                   | 417 ms                                                 | 533 ms: 1.28x slower                                                       |
| pprint_safe_repr           | 776 ms                                                 | 998 ms: 1.29x slower                                                       |
| 2to3                       | 274 ms                                                 | 353 ms: 1.29x slower                                                       |
| telco                      | 7.10 ms                                                | 9.15 ms: 1.29x slower                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 191 ms: 1.30x slower                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 951 ms: 1.31x slower                                                       |
| pprint_pformat             | 1.57 sec                                               | 2.07 sec: 1.32x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 13.7 ms: 1.32x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 209 us: 1.33x slower                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 25.1 ms: 1.34x slower                                                      |
| django_template            | 34.6 ms                                                | 47.3 ms: 1.37x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 233 ms: 1.38x slower                                                       |
| unpickle_pure_python       | 230 us                                                 | 320 us: 1.39x slower                                                       |
| logging_format             | 7.23 us                                                | 10.1 us: 1.39x slower                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 805 ms: 1.40x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 9.76 ms: 1.41x slower                                                      |
| sympy_expand               | 478 ms                                                 | 673 ms: 1.41x slower                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.03 sec: 1.42x slower                                                     |
| logging_simple             | 6.46 us                                                | 9.26 us: 1.43x slower                                                      |
| nbody                      | 97.0 ms                                                | 139 ms: 1.43x slower                                                       |
| pyflate                    | 482 ms                                                 | 693 ms: 1.44x slower                                                       |
| pickle_pure_python         | 324 us                                                 | 475 us: 1.46x slower                                                       |
| coverage                   | 72.7 ms                                                | 107 ms: 1.47x slower                                                       |
| chaos                      | 67.0 ms                                                | 99.7 ms: 1.49x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 176 ms: 1.49x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 679 ms: 1.51x slower                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 113 ms: 1.51x slower                                                       |
| hexiom                     | 6.41 ms                                                | 9.72 ms: 1.52x slower                                                      |
| async_tree_memoization     | 578 ms                                                 | 884 ms: 1.53x slower                                                       |
| richards                   | 45.8 ms                                                | 70.2 ms: 1.53x slower                                                      |
| richards_super             | 51.5 ms                                                | 79.1 ms: 1.53x slower                                                      |
| mako                       | 11.9 ms                                                | 18.4 ms: 1.54x slower                                                      |
| float                      | 84.7 ms                                                | 131 ms: 1.54x slower                                                       |
| mypy2                      | 830 ms                                                 | 1.29 sec: 1.55x slower                                                     |
| async_tree_none            | 472 ms                                                 | 733 ms: 1.55x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.32 ms: 1.57x slower                                                      |
| raytrace                   | 312 ms                                                 | 505 ms: 1.62x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.78 ms: 1.65x slower                                                      |
| logging_silent             | 104 ns                                                 | 173 ns: 1.66x slower                                                       |
| python_startup             | 9.55 ms                                                | 16.3 ms: 1.70x slower                                                      |
| go                         | 139 ms                                                 | 243 ms: 1.74x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 2.42 ms: 1.78x slower                                                      |
| scimark_sor                | 129 ms                                                 | 237 ms: 1.84x slower                                                       |
| deltablue                  | 3.72 ms                                                | 7.56 ms: 2.03x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 3.59 ms: 4.26x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 102 ms: 4.26x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.32x slower                                                               |

Benchmark hidden because not significant (3): deepcopy_memo, gc_traversal, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241215-3.14.0a2+-a0a0f85-NOGIL/bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.221x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: 1.33x