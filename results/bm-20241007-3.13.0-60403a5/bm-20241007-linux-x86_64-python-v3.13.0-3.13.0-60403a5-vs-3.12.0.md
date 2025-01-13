# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                   |
| chameleon      | 7.41 ms                                                | 6.81 ms: 1.09x faster                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                 |
| tornado_http   | 103 ms                                                 | 91.2 ms: 1.12x faster                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                   |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                   |
| async_tree_none            | 472 ms                                                 | 350 ms: 1.35x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 463 ms: 1.24x faster                                   |
| Geometric mean             | (ref)                                                  | 1.33x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.7 ms: 1.11x faster                                  |
| float          | 84.7 ms                                                | 78.7 ms: 1.08x faster                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                   |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                  |
| regex_v8       | 23.1 ms                                                | 26.9 ms: 1.16x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                 |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                   |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                   |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                  |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                  |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                   |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                   |
| async_tree_none            | 472 ms                                                 | 350 ms: 1.35x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 437 ms: 1.32x faster                                   |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 463 ms: 1.24x faster                                   |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                   |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                  |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                  |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                  |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                  |
| tornado_http               | 103 ms                                                 | 91.2 ms: 1.12x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                  |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                   |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                   |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                  |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                  |
| nbody                      | 97.0 ms                                                | 87.7 ms: 1.11x faster                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                   |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                 |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.7 ms: 1.10x faster                                  |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                  |
| chameleon                  | 7.41 ms                                                | 6.81 ms: 1.09x faster                                  |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.09x faster                                  |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                   |
| float                      | 84.7 ms                                                | 78.7 ms: 1.08x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                   |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                 |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                   |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 38.4 us: 1.06x faster                                  |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                 |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                  |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                   |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                   |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.06x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                  |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                   |
| gunicorn                   | 1.24 ms                                                | 1.18 ms: 1.05x faster                                  |
| deepcopy                   | 371 us                                                 | 354 us: 1.05x faster                                   |
| coroutines                 | 23.2 ms                                                | 22.2 ms: 1.04x faster                                  |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                   |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                   |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.24 us: 1.03x faster                                  |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                   |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                   |
| nqueens                    | 83.3 ms                                                | 80.9 ms: 1.03x faster                                  |
| bench_thread_pool          | 842 us                                                 | 818 us: 1.03x faster                                   |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                   |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.03 ms: 1.01x faster                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                   |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                   |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                 |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| richards                   | 45.8 ms                                                | 47.5 ms: 1.04x slower                                  |
| richards_super             | 51.5 ms                                                | 53.7 ms: 1.04x slower                                  |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                  |
| coverage                   | 72.7 ms                                                | 82.8 ms: 1.14x slower                                  |
| regex_v8                   | 23.1 ms                                                | 26.9 ms: 1.16x slower                                  |
| telco                      | 7.10 ms                                                | 8.40 ms: 1.18x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.90 ms: 1.29x slower                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x