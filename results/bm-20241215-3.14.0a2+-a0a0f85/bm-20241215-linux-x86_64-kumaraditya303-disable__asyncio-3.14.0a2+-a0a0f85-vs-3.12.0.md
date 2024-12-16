# Results vs. 3.12.0

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.038x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                       |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 1.03 sec: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 489 ms: 1.09x slower                                                       |
| async_tree_memoization     | 578 ms                                                 | 632 ms: 1.09x slower                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 796 ms: 1.10x slower                                                       |
| async_tree_none            | 472 ms                                                 | 522 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                      |
| nbody          | 97.0 ms                                                | 91.8 ms: 1.06x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.08x faster                                                      |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.2 ms: 1.10x faster                                                      |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                       |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                      |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                                     |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| generators                 | 31.2 ms                                                | 27.2 ms: 1.15x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                       |
| go                         | 139 ms                                                 | 122 ms: 1.15x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 72.7 ms: 1.13x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 1.03 sec: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.11x faster                                                     |
| float                      | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 97.2 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                      |
| async_generators           | 463 ms                                                 | 423 ms: 1.10x faster                                                       |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                      |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                      |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.08x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                       |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                      |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| nbody                      | 97.0 ms                                                | 91.8 ms: 1.06x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                      |
| nqueens                    | 83.3 ms                                                | 79.0 ms: 1.05x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                     |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                       |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                      |
| pyflate                    | 482 ms                                                 | 462 ms: 1.04x faster                                                       |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 65.7 ms: 1.04x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                     |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 52.8 ms: 1.04x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                      |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                       |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.01x slower                                                      |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                      |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 858 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                       |
| richards_super             | 51.5 ms                                                | 53.1 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 489 ms: 1.09x slower                                                       |
| async_tree_memoization     | 578 ms                                                 | 632 ms: 1.09x slower                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 796 ms: 1.10x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                      |
| async_tree_none            | 472 ms                                                 | 522 ms: 1.11x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| mypy2                      | 830 ms                                                 | 942 ms: 1.13x slower                                                       |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, coroutines, mdp, asyncio_websockets, sqlite_synth, async_tree_memoization_tg
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241215-3.14.0a2+-a0a0f85/bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x