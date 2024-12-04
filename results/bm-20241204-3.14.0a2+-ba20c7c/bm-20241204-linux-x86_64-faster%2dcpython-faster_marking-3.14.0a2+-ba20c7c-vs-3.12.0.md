# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: ba20c7c
- commit date: 2024-12-04
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                       |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 344 ms: 1.67x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 350 ms: 1.65x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.7 ms: 1.05x faster                                                      |
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                      |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                      |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                       |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                     |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 88.3 ms: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                      |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                       |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 344 ms: 1.67x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 350 ms: 1.65x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                       |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.32x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                      |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                      |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                      |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                       |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                                      |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.09x faster                                                      |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                     |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                      |
| json                       | 5.26 ms                                                | 4.89 ms: 1.08x faster                                                      |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                      |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                     |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 64.9 ms: 1.06x faster                                                      |
| float                      | 84.7 ms                                                | 80.7 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                      |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                      |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                       |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                      |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                       |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                                      |
| pyflate                    | 482 ms                                                 | 475 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 54.1 ms: 1.01x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 88.3 ms: 1.01x faster                                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 854 us: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                      |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                       |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                      |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                       |
| richards_super             | 51.5 ms                                                | 53.3 ms: 1.03x slower                                                      |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.27 ms: 1.54x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, asyncio_websockets, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241204-3.14.0a2+-ba20c7c/bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x