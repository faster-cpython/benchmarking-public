# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.063x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                       |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                     |
| tornado_http   | 103 ms                                                 | 94.3 ms: 1.09x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                       |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.41x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                       |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 966 ms: 1.22x faster                                       |
| Geometric mean             | (ref)                                                  | 1.36x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.3 ms: 1.19x faster                                      |
| float          | 84.7 ms                                                | 75.4 ms: 1.12x faster                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| regex_dna      | 212 ms                                                 | 217 ms: 1.03x slower                                       |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                     |
| xml_etree_generate   | 89.2 ms                                                | 78.6 ms: 1.13x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                       |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.9 ms: 1.07x faster                                      |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                       |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                      |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                       |
| pickle_dict          | 35.5 us                                                | 35.8 us: 1.01x slower                                      |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                      |
| pickle               | 11.6 us                                                | 12.0 us: 1.03x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| unpickle_list        | 5.29 us                                                | 5.59 us: 1.06x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                      |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                      |
| Geometric mean         | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                      |
| django_template | 34.6 ms                                                | 37.2 ms: 1.08x slower                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                       |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.41x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                      |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                       |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                       |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 966 ms: 1.22x faster                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                      |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                      |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                       |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                      |
| nbody                      | 97.0 ms                                                | 81.3 ms: 1.19x faster                                      |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                      |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                      |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 78.6 ms: 1.13x faster                                      |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                      |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                      |
| float                      | 84.7 ms                                                | 75.4 ms: 1.12x faster                                      |
| richards                   | 45.8 ms                                                | 41.0 ms: 1.12x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                      |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                       |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                       |
| tornado_http               | 103 ms                                                 | 94.3 ms: 1.09x faster                                      |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                       |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                      |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                     |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 99.9 ms: 1.07x faster                                      |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                       |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                      |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                      |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                       |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                       |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                       |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                       |
| dulwich_log                | 68.5 ms                                                | 66.5 ms: 1.03x faster                                      |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                      |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                       |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                      |
| pickle_dict                | 35.5 us                                                | 35.8 us: 1.01x slower                                      |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                       |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                     |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                     |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                       |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                      |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.03x slower                                       |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                       |
| async_generators           | 463 ms                                                 | 478 ms: 1.03x slower                                       |
| pickle                     | 11.6 us                                                | 12.0 us: 1.03x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                      |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                       |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                       |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                       |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                     |
| unpickle_list              | 5.29 us                                                | 5.59 us: 1.06x slower                                      |
| django_template            | 34.6 ms                                                | 37.2 ms: 1.08x slower                                      |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                      |
| hexiom                     | 6.41 ms                                                | 7.03 ms: 1.10x slower                                      |
| sqlglot_optimize           | 54.8 ms                                                | 60.2 ms: 1.10x slower                                      |
| sympy_integrate            | 21.4 ms                                                | 23.6 ms: 1.10x slower                                      |
| generators                 | 31.2 ms                                                | 35.4 ms: 1.14x slower                                      |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.40 ms: 1.16x slower                                      |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                      |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                      |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.04x slower                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (2): sqlglot_transpile, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.063x faster
# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x