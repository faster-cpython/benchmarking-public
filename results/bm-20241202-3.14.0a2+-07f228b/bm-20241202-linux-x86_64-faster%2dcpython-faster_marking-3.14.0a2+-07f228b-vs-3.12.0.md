# Results vs. 3.12.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 07f228b
- commit date: 2024-12-02
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 636 ms: 1.82x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 683 ms: 1.73x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 352 ms: 1.64x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                       |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 286 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 522 ms: 1.39x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.60x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                      |
| nbody          | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                      |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 86.5 ms: 1.03x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                      |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 636 ms: 1.82x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 683 ms: 1.73x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 352 ms: 1.64x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                       |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 286 ms: 1.57x faster                                                       |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 522 ms: 1.39x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| go                         | 139 ms                                                 | 118 ms: 1.19x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                                      |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                      |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                      |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                      |
| async_generators           | 463 ms                                                 | 424 ms: 1.09x faster                                                       |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                      |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                      |
| json                       | 5.26 ms                                                | 4.85 ms: 1.09x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                      |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                     |
| pyflate                    | 482 ms                                                 | 453 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.06x faster                                                      |
| float                      | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                      |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 86.5 ms: 1.03x faster                                                      |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                      |
| nbody                      | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.03x faster                                                      |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                       |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 851 us: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                       |
| richards                   | 45.8 ms                                                | 46.8 ms: 1.02x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                     |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                      |
| richards_super             | 51.5 ms                                                | 53.1 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                       |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                                       |
| logging_silent             | 104 ns                                                 | 108 ns: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| coverage                   | 72.7 ms                                                | 83.4 ms: 1.15x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.66 ms: 1.23x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.43 ms: 1.64x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (2): scimark_lu, scimark_sor
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241202-3.14.0a2+-07f228b/bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x