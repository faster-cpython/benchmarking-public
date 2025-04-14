# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                       |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                     |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                       |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.44x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                       |
| async_tree_io              | 1.16 sec                                               | 852 ms: 1.36x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 968 ms: 1.22x faster                                       |
| Geometric mean             | (ref)                                                  | 1.36x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.8 ms: 1.09x faster                                      |
| float          | 84.7 ms                                                | 79.2 ms: 1.07x faster                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                       |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                     |
| pickle_dict          | 35.5 us                                                | 33.3 us: 1.07x faster                                      |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                       |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                      |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                      |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.5 ms: 1.02x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.01x faster                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| unpickle_list        | 5.29 us                                                | 5.49 us: 1.04x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                      |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                       |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.44x faster                                       |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                       |
| async_tree_io              | 1.16 sec                                               | 852 ms: 1.36x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 575 ms: 1.26x faster                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 968 ms: 1.22x faster                                       |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                      |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                       |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                      |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                      |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                       |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                       |
| generators                 | 31.2 ms                                                | 27.0 ms: 1.16x faster                                      |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                       |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                      |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                       |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                     |
| unpack_sequence            | 54.0 ns                                                | 48.5 ns: 1.11x faster                                      |
| nbody                      | 97.0 ms                                                | 88.8 ms: 1.09x faster                                      |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                      |
| dulwich_log                | 68.5 ms                                                | 63.5 ms: 1.08x faster                                      |
| float                      | 84.7 ms                                                | 79.2 ms: 1.07x faster                                      |
| pickle_dict                | 35.5 us                                                | 33.3 us: 1.07x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                       |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                       |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                       |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                      |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                       |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.05x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                       |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                     |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                      |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                     |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                       |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                       |
| nqueens                    | 83.3 ms                                                | 79.9 ms: 1.04x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                     |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                       |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                       |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                      |
| async_generators           | 463 ms                                                 | 447 ms: 1.04x faster                                       |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                      |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                       |
| pyflate                    | 482 ms                                                 | 471 ms: 1.03x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.5 ms: 1.02x faster                                      |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                      |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.01x faster                                       |
| asyncio_tcp                | 491 ms                                                 | 486 ms: 1.01x faster                                       |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                     |
| pickle_list                | 5.08 us                                                | 5.10 us: 1.00x slower                                      |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                       |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                      |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                      |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.01x slower                                     |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                       |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.02x slower                                      |
| unpickle_list              | 5.29 us                                                | 5.49 us: 1.04x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                      |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                      |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.54 ms: 1.20x slower                                      |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                      |
| bench_mp_pool              | 24.0 ms                                                | 77.9 ms: 3.25x slower                                      |
| Geometric mean             | (ref)                                                  | 1.05x faster                                               |

Benchmark hidden because not significant (3): coroutines, regex_effbot, richards
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.073x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x