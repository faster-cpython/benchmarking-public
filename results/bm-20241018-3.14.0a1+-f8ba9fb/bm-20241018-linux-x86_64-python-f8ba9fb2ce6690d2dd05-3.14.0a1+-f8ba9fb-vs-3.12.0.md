# Results vs. 3.12.0

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                   |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 851 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 563 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 975 ms: 1.21x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.9 ms: 1.06x faster                                                  |
| nbody          | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| unpickle             | 15.9 us                                                | 14.6 us: 1.09x faster                                                  |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                   |
| pickle_dict          | 35.5 us                                                | 33.9 us: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.02x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.57 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| mako            | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                   |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                   |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 851 ms: 1.36x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.1 us: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 563 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 975 ms: 1.21x faster                                                   |
| unpack_sequence            | 54.0 ns                                                | 44.6 ns: 1.21x faster                                                  |
| logging_format             | 7.23 us                                                | 6.21 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                  |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                   |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.0 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.09x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                  |
| json                       | 5.26 ms                                                | 4.87 ms: 1.08x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 63.4 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                  |
| float                      | 84.7 ms                                                | 79.9 ms: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.9 us: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                   |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                   |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                   |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                 |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 846 us: 1.00x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                   |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.21 us: 1.02x slower                                                  |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.57 us: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                  |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 78.0 ms: 3.25x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (5): scimark_sor, richards, scimark_sparse_mat_mult, mdp, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241018-3.14.0a1+-f8ba9fb/bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x