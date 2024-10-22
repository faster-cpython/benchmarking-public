# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| tornado_http   | 103 ms                                                 | 92.5 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 417 ms: 1.38x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 578 ms: 1.26x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.4 ms: 1.07x faster                                                    |
| nbody          | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                    |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.14x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.02x faster                                                    |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                   |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                    |
| unpickle             | 15.9 us                                                | 15.4 us: 1.03x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                    |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                                     |
| unpickle_list        | 5.29 us                                                | 5.23 us: 1.01x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                    |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                    |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                     |
| deepcopy                   | 371 us                                                 | 266 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 417 ms: 1.38x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 886 ms: 1.34x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.30x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.29x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 578 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.21x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                    |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                     |
| unpack_sequence            | 54.0 ns                                                | 46.6 ns: 1.16x faster                                                    |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                     |
| regex_compile              | 148 ms                                                 | 131 ms: 1.14x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                    |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.80 us: 1.11x faster                                                    |
| tornado_http               | 103 ms                                                 | 92.5 ms: 1.11x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                    |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.08x faster                                                     |
| chaos                      | 67.0 ms                                                | 62.1 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                    |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                    |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                    |
| float                      | 84.7 ms                                                | 79.4 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                    |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| scimark_fft                | 382 ms                                                 | 361 ms: 1.06x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 65.4 ms: 1.05x faster                                                    |
| async_generators           | 463 ms                                                 | 444 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                    |
| nbody                      | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                    |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                    |
| unpickle                   | 15.9 us                                                | 15.4 us: 1.03x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 86.6 ms: 1.03x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                    |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                     |
| asyncio_tcp                | 491 ms                                                 | 483 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 763 ms: 1.02x faster                                                     |
| nqueens                    | 83.3 ms                                                | 82.0 ms: 1.02x faster                                                    |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                    |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.23 us: 1.01x faster                                                    |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                    |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                    |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.00x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                     |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.01x slower                                                   |
| pyflate                    | 482 ms                                                 | 490 ms: 1.01x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 858 us: 1.02x slower                                                     |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                    |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                     |
| richards                   | 45.8 ms                                                | 47.3 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                     |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                    |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                    |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.16x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (4): pprint_pformat, sqlglot_optimize, fannkuch, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241011-3.14.0a0-35db580/bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.97x