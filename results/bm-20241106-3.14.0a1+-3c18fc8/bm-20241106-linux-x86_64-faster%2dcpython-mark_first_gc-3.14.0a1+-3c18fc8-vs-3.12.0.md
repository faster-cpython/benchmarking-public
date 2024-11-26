# Results vs. 3.12.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 3c18fc8
- commit date: 2024-11-06
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                      |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 334 ms: 1.73x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                     |
| nbody          | 97.0 ms                                                | 95.3 ms: 1.02x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                    |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.78 ms: 1.02x faster                                                     |
| python_startup         | 9.55 ms                                                | 12.3 ms: 1.29x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                     |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 334 ms: 1.73x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 2.32 ms: 1.64x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                      |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                     |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                     |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                      |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                     |
| generators                 | 31.2 ms                                                | 26.7 ms: 1.17x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 73.4 ms: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                     |
| json                       | 5.26 ms                                                | 4.76 ms: 1.11x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                     |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                      |
| float                      | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                     |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                     |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                     |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                      |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| python_startup_no_site     | 6.94 ms                                                | 6.78 ms: 1.02x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                     |
| scimark_fft                | 382 ms                                                 | 375 ms: 1.02x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                                     |
| nbody                      | 97.0 ms                                                | 95.3 ms: 1.02x faster                                                     |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                     |
| richards                   | 45.8 ms                                                | 45.5 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 841 us: 1.00x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                      |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.01x slower                                                     |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.19 ms: 1.03x slower                                                     |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| telco                      | 7.10 ms                                                | 8.00 ms: 1.13x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                     |
| coverage                   | 72.7 ms                                                | 86.1 ms: 1.18x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.3 ms: 1.29x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 80.2 ms: 3.34x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (4): scimark_sor, sqlite_synth, scimark_lu, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241106-3.14.0a1+-3c18fc8/bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.112x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x