# Results vs. 3.12.0

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                     |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                     |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                                    |
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                    |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                    |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                     |
| regex_v8       | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                     |
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                                    |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                    |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                     |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                     |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.35x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                    |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                    |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                                    |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                                    |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                    |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                   |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                                    |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                                    |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                     |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                    |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 64.9 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.06x faster                                                     |
| json                       | 5.26 ms                                                | 4.99 ms: 1.05x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                     |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                     |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                    |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                   |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                    |
| scimark_fft                | 382 ms                                                 | 370 ms: 1.03x faster                                                     |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                    |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                     |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                    |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                    |
| richards                   | 45.8 ms                                                | 46.6 ms: 1.02x slower                                                    |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                     |
| richards_super             | 51.5 ms                                                | 52.6 ms: 1.02x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                    |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.8 ms: 1.16x slower                                                    |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): spectral_norm
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.096x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x