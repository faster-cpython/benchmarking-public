# Results vs. 3.12.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 5e813c5
- commit date: 2024-11-04
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                      |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 658 ms: 1.80x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                     |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                      |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 151 ms: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 658 ms: 1.80x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                      |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 32.0 us: 1.27x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                     |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                      |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                     |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                                     |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                     |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.08x faster                                                     |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                      |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 64.2 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 151 ms: 1.06x faster                                                      |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                    |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                      |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                     |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                     |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                      |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                     |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.01x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                     |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                      |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 840 us: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| scimark_fft                | 382 ms                                                 | 387 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                     |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                                     |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                      |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                    |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                     |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                      |
| richards                   | 45.8 ms                                                | 48.2 ms: 1.05x slower                                                     |
| richards_super             | 51.5 ms                                                | 54.6 ms: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                     |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.47 ms: 1.18x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): pycparser, django_template
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241104-3.14.0a1+-5e813c5/bm-20241104-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-5e813c5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.085x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x