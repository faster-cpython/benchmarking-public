# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 8262bf0
- commit date: 2024-12-04
- overall geometric mean: 1.097x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                       |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                       |
| async_tree_none            | 472 ms                                                 | 273 ms: 1.73x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 336 ms: 1.71x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 268 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.68x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                      |
| nbody          | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                      |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                                      |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 60.9 ms: 1.01x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                      |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                       |
| async_tree_none            | 472 ms                                                 | 273 ms: 1.73x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 336 ms: 1.71x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 268 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                       |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                                      |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                       |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                      |
| async_generators           | 463 ms                                                 | 423 ms: 1.09x faster                                                       |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                      |
| json                       | 5.26 ms                                                | 4.85 ms: 1.08x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                      |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                      |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 64.7 ms: 1.06x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                     |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                      |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                       |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                       |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                       |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                      |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 60.9 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| nbody                      | 97.0 ms                                                | 96.3 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 849 us: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                      |
| richards                   | 45.8 ms                                                | 46.6 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.17 ms: 1.02x slower                                                      |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                      |
| richards_super             | 51.5 ms                                                | 52.9 ms: 1.03x slower                                                      |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.45 ms: 1.17x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.23 ms: 1.51x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                               |

Benchmark hidden because not significant (1): pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241204-3.14.0a2+-8262bf0/bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.097x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x